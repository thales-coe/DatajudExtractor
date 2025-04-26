import tkinter as tk
from tkinter import messagebox, filedialog
from tkcalendar import DateEntry
import datetime
import requests
import pandas as pd
import time

# Configurações da API
API_KEY = "cDZHYzlZa0JadVREZDJCendQbXY6SkJlTzNjLV9TRENyQk1RdnFKZGRQdw=="
DATAJUD_URL = "https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search"
HEADERS = {"Authorization": f"APIKey {API_KEY}", "Content-Type": "application/json"}

class DatajudApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Datajud Extractor")
        self.geometry("480x400")
        self.resizable(False, False)
        self._build_initial_ui()

    def _build_initial_ui(self):
        # Limpa tela
        for widget in self.winfo_children():
            widget.destroy()

        # Texto de boas-vindas
        welcome = (
            "Bem-vindo ao Datajud Extractor 1.0\n\n"
            "Este é um projeto Open Source, desenvolvido por Thales Coelho,\n"
            "voltado à extração de metadados de processos judiciais via API pública Datajud.\n"
            "v.1.0 - Busca na API DATAJUD de processos com assunto '12484 Fornecimento de medicamentos' no TJSP\n\n"

            "Selecione o período desejado e exporte os resultados em Excel."
        )
        tk.Label(self, text=welcome, wraplength=440, justify="center").pack(pady=10)

        # Seleção de datas
        frame = tk.Frame(self)
        frame.pack(pady=10)
        today = datetime.date.today()
        default_start = today.replace(day=1)
        tk.Label(frame, text="Data Início (DD-MM-YYYY)").grid(row=0, column=0, padx=5, pady=5)
        self.start_date = DateEntry(
            frame, date_pattern='dd-MM-yyyy',
            year=default_start.year, month=default_start.month, day=default_start.day
        )
        self.start_date.grid(row=0, column=1, padx=5)
        tk.Label(frame, text="Data Final (DD-MM-YYYY)").grid(row=1, column=0, padx=5, pady=5)
        self.end_date = DateEntry(
            frame, date_pattern='dd-MM-yyyy',
            year=today.year, month=today.month, day=today.day
        )
        self.end_date.grid(row=1, column=1, padx=5)

        # Botão Buscar
        tk.Button(self, text="Buscar e Exportar", command=self.buscar_exportar, width=20).pack(pady=15)

        # Rodapé
        tk.Label(self, text="Licença: CC BY-SA | Desenvolvido por Thales Coelho", font=(None, 8)).pack(side="bottom", pady=5)

    def buscar_exportar(self):
        data_inicio = self.start_date.get_date().strftime("%Y-%m-%d")
        data_fim    = self.end_date.get_date().strftime("%Y-%m-%d")

        # Medir tempo de busca
        t0 = time.perf_counter()
        try:
            df = self.fetch_datajud(data_inicio, data_fim)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao buscar dados: {e}")
            return
        t1 = time.perf_counter()
        api_time = t1 - t0

        total = len(df)
        if total == 0:
            messagebox.showinfo("Nenhum Resultado", "Nenhum processo encontrado neste período.")
            return

        export_time = 0
        # Pergunta ao usuário para salvar
        if messagebox.askyesno(
            "Resultados Encontrados",
            f"Foram encontrados {total} processos.\nDeseja exportar para Excel?"
        ):
            # Salvar e medir tempo de exportação
            default_name = f"medicamentos_{self.start_date.get_date().strftime('%d-%m-%Y')}_a_{self.end_date.get_date().strftime('%d-%m-%Y')}.xlsx"
            path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx")],
                initialfile=default_name,
                title="Salvar como"
            )
            if path:
                t2 = time.perf_counter()
                try:
                    df.to_excel(path, index=False)
                    t3 = time.perf_counter()
                    export_time = t3 - t2
                except Exception as e:
                    messagebox.showerror("Erro", f"Falha ao salvar arquivo: {e}")
                    return

        # Exibir estatísticas na mesma janela
        self._show_stats(api_time, export_time)

    def _show_stats(self, api_time, export_time):
        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Operação Concluída", font=(None, 14)).pack(pady=10)
        stats = (
            f"Tempo de pesquisa na API: {api_time:.2f} segundos\n"
            f"Tempo de geração do Excel: {export_time:.2f} segundos"
        )
        tk.Label(self, text=stats, justify="center").pack(pady=10)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=20)
        tk.Button(btn_frame, text="Nova Pesquisa", command=self._build_initial_ui, width=18).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Fechar", command=self.destroy, width=18).grid(row=0, column=1, padx=10)

    def fetch_datajud(self, data_inicio, data_fim):
        resultados = []
        search_after = None
        gte = f"{data_inicio}T00:00:00"
        lte = f"{data_fim}T23:59:59"
        while True:
            payload = {
                "query": {"bool": {"must": [
                    {"term": {"tribunal.keyword": "TJSP"}},
                    {"term": {"assuntos.codigo": 12484}},
                    {"range": {"dataAjuizamento": {"gte": gte, "lte": lte}}}
                ]}},
                "size": 100,
                "sort": [{"dataAjuizamento": "asc"}, {"numeroProcesso.keyword": "asc"}]
            }
            if search_after:
                payload["search_after"] = search_after
            resp = requests.post(DATAJUD_URL, headers=HEADERS, json=payload)
            resp.raise_for_status()
            hits = resp.json().get("hits", {}).get("hits", [])
            if not hits:
                break
            for hit in hits:
                src = hit.get("_source", {})
                resultados.append({
                    "numeroProcesso": src.get("numeroProcesso"),
                    "dataAjuizamento": src.get("dataAjuizamento"),
                    "grau": src.get("grau"),
                    "orgaoJulgador": src.get("orgaoJulgador", {}).get("nomeOrgao")
                })
            search_after = hits[-1].get("sort")
        return pd.DataFrame(resultados)

if __name__ == "__main__":
    # Dependências: pip install requests pandas openpyxl tkcalendar
    app = DatajudApp()
    app.mainloop()
