import tkinter as tk
from tkinter import scrolledtext

def setup_ui(run_simulation_callback, reset_totals_callback):
    root = tk.Tk()
    root.title("로또 시뮬레이션")

    # 로또 장수 입력
    frame = tk.Frame(root)
    frame.pack(pady=10)

    label = tk.Label(frame, text="로또 장수:")
    label.pack(side="left", padx=5)

    entry_count = tk.Entry(frame, width=10)
    entry_count.pack(side="left", padx=5)

    result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
    result_text.pack(fill="both", expand=True, pady=10)

    def run_simulation_wrapper():
        run_simulation_callback(entry_count, result_text)

    def reset_totals_wrapper():
        reset_totals_callback()
        result_text.delete("1.0", "end")

    run_button = tk.Button(frame, text="시뮬레이션 실행", command=run_simulation_wrapper)
    run_button.pack(side="left", padx=5)

    reset_button = tk.Button(frame, text="초기화", command=reset_totals_wrapper)
    reset_button.pack(side="left", padx=5)

    root.mainloop()
