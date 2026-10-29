import tkinter as tk
from tkinter import messagebox

RATES = {
    "USD": {"buy": 41.20, "sell": 41.70},
    "EUR": {"buy": 44.50, "sell": 45.10},
}


class CurrencyExchange:

    def __init__(self, root):
        self.root = root
        self.root.title("Обмін валюти та Гаманець")
        self.root.geometry("400x520")
        self.root.resizable(False, False)


        self.wallet = {"UAH": 10000.00, "USD": 100.00, "EUR": 50.00}


        wallet_frame = tk.LabelFrame(
            root,
            text=" Ваш Гаманець ",
            font=("Times New Roman", 10, "bold"),
            padx=10,
            pady=5,
        )
        wallet_frame.pack(fill=tk.X, padx=20, pady=10)

        self.lbl_wallet_uah = tk.Label(
            wallet_frame,
            text="",
            font=("Times New Roman", 10),
            fg="darkgreen",
        )
        self.lbl_wallet_uah.pack(anchor="w")

        self.lbl_wallet_usd = tk.Label(
            wallet_frame, text="", font=("Times New Roman", 10)
        )
        self.lbl_wallet_usd.pack(anchor="w")

        self.lbl_wallet_eur = tk.Label(
            wallet_frame, text="", font=("Times New Roman", 10)
        )
        self.lbl_wallet_eur.pack(anchor="w")


        self.update_wallet_ui()


        tk.Label(
            root, text="Оберіть валюту:", font=("Times New Roman", 10, "bold")
        ).pack(anchor="w", padx=20, pady=(5, 2))
        self.currency_var = tk.StringVar(value="USD")

        curr_frame = tk.Frame(root)
        curr_frame.pack(anchor="w", padx=20)
        tk.Radiobutton(
            curr_frame,
            text="USD ",
            variable=self.currency_var,
            value="USD",
            command=self.update_rates,
        ).pack(side=tk.LEFT)
        tk.Radiobutton(
            curr_frame,
            text="EUR ",
            variable=self.currency_var,
            value="EUR",
            command=self.update_rates,
        ).pack(side=tk.LEFT, padx=15)


        tk.Label(
            root, text="Операція:", font=("Times New Roman", 10, "bold")
        ).pack(anchor="w", padx=20, pady=(10, 2))
        self.operation_var = tk.StringVar(value="buy")

        op_frame = tk.Frame(root)
        op_frame.pack(anchor="w", padx=20)
        tk.Radiobutton(
            op_frame,
            text="Купівля (Ви купуєте валюту)",
            variable=self.operation_var,
            value="buy",
            command=self.update_rates,
        ).pack(anchor="w")
        tk.Radiobutton(
            op_frame,
            text="Продаж (Ви продаєте валюту)",
            variable=self.operation_var,
            value="sell",
            command=self.update_rates,
        ).pack(anchor="w")

        self.lbl_rate = tk.Label(
            root, text="", font=("Times New Roman", 9, "italic"), fg="blue"
        )
        self.lbl_rate.pack(anchor="w", padx=20, pady=5)


        tk.Label(root, text="Сума валюти:").pack(anchor="w", padx=20)
        self.entry_amount = tk.Entry(root, font=("Times New Roman", 10))
        self.entry_amount.pack(fill=tk.X, padx=20, pady=2)

        self.lbl_result = tk.Label(
            root,
            text="До сплати: 0.00 грн",
            font=("Times New Roman", 11, "bold"),
            fg="green",
        )
        self.lbl_result.pack(pady=10)


        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Здійснити обмін",
            command=self.calculate,
            width=15,
            bg="#e1e1e1",
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            btn_frame,
            text="Закінчити роботу",
            command=root.quit,
            width=15,
            bg="#ffcccc",
        ).pack(side=tk.LEFT, padx=5)

        self.update_rates()

    def update_wallet_ui(self):
        """Оновлює текст із балансом у вікні"""
        self.lbl_wallet_uah.config(
            text=f"Гривні (UAH): {self.wallet['UAH']:.2f} грн"
        )
        self.lbl_wallet_usd.config(
            text=f"Долари (USD): {self.wallet['USD']:.2f} $"
        )
        self.lbl_wallet_eur.config(
            text=f"Євро (EUR): {self.wallet['EUR']:.2f} €"
        )

    def update_rates(self):
        curr = self.currency_var.get()
        op = self.operation_var.get()
        rate = RATES[curr][op]
        op_name = "купівлі" if op == "buy" else "продажу"
        self.lbl_rate.config(text=f"Поточний курс {op_name} {curr}: {rate} грн")

    def calculate(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError

            curr = self.currency_var.get()
            op = self.operation_var.get()
            rate = RATES[curr][op]

            total_cost_uah = amount * rate


            if op == "buy":
                if self.wallet["UAH"] < total_cost_uah:
                    messagebox.showerror(
                        "Недостатньо коштів",
                        f"У вас недостатньо UAH! Потрібно {total_cost_uah:.2f} грн, а у вас є лише {self.wallet['UAH']:.2f} грн.",
                    )
                    return

                self.wallet["UAH"] -= total_cost_uah
                self.wallet[curr] += amount
                messagebox.showinfo(
                    "Успіх",
                    f"Ви успішно купили {amount:.2f} {curr} за {total_cost_uah:.2f} грн!",
                )

            elif op == "sell":

                if self.wallet[curr] < amount:
                    messagebox.showerror(
                        "Недостатньо коштів",
                        f"У вас недостатньо {curr}! Потрібно {amount:.2f} {curr}, а у вас є лише {self.wallet[curr]:.2f} {curr}.",
                    )
                    return

                self.wallet[curr] -= amount
                self.wallet["UAH"] += total_cost_uah
                messagebox.showinfo(
                    "Успіх",
                    f"Ви успішно продали {amount:.2f} {curr} та отримали {total_cost_uah:.2f} грн!",
                )


            self.lbl_result.config(text=f"Сума операції: {total_cost_uah:.2f} грн")
            self.update_wallet_ui()

        except ValueError:
            messagebox.showerror(
                "Помилка", "Введіть коректну позитивну суму!"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyExchange(root)
    root.mainloop()