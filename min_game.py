import tkinter as tk
import random

# ---------------- MAIN APP ----------------
root = tk.Tk()
root.title("Mini Game Hub 🎮")
root.geometry("350x400")
root.config(bg="#1e1e2e")

# ---------------- CLEAR SCREEN ----------------
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------- MAIN MENU ----------------
def main_menu():
    clear()

    tk.Label(root, text="🎮 MINI GAME HUB",
             font=("Arial", 18, "bold"),
             fg="white", bg="#1e1e2e").pack(pady=20)

    tk.Button(root, text="🎯 Number Guessing",
              width=25, command=number_game).pack(pady=10)

    tk.Button(root, text="✊✋✌️ Rock Paper Scissors",
              width=25, command=rps_game).pack(pady=10)

    tk.Button(root, text="❌⭕ Tic Tac Toe",
              width=25, command=tic_tac_toe).pack(pady=10)

# ---------------- 1. NUMBER GAME ----------------
def number_game():
    clear()
    number = random.randint(1, 100)

    tk.Label(root, text="Guess (1-100)",
             bg="#1e1e2e", fg="white",
             font=("Arial", 14)).pack(pady=10)

    entry = tk.Entry(root)
    entry.pack()

    result = tk.Label(root, text="", bg="#1e1e2e", fg="yellow")
    result.pack(pady=10)

    def check():
        try:
            guess = int(entry.get())
            if guess < number:
                result.config(text="📉 Too Low!")
            elif guess > number:
                result.config(text="📈 Too High!")
            else:
                result.config(text="🎉 Correct!")
        except:
            result.config(text="⚠ Enter valid number!")

    tk.Button(root, text="Check", command=check).pack(pady=5)
    tk.Button(root, text="⬅ Back", command=main_menu).pack(pady=10)

# ---------------- 2. RPS GAME ----------------
def rps_game():
    clear()

    choices = ["Rock", "Paper", "Scissors"]

    tk.Label(root, text="✊✋✌️ RPS GAME",
             bg="#1e1e2e", fg="white",
             font=("Arial", 14)).pack(pady=10)

    result = tk.Label(root, text="", bg="#1e1e2e", fg="yellow")
    result.pack(pady=10)

    def play(user):
        comp = random.choice(choices)

        if user == comp:
            msg = f"🤝 Draw! CPU chose {comp}"
        elif (user == "Rock" and comp == "Scissors") or \
             (user == "Paper" and comp == "Rock") or \
             (user == "Scissors" and comp == "Paper"):
            msg = f"🎉 You Win! CPU chose {comp}"
        else:
            msg = f"💀 You Lose! CPU chose {comp}"

        result.config(text=msg)

    tk.Button(root, text="Rock", command=lambda: play("Rock")).pack()
    tk.Button(root, text="Paper", command=lambda: play("Paper")).pack()
    tk.Button(root, text="Scissors", command=lambda: play("Scissors")).pack()

    tk.Button(root, text="⬅ Back", command=main_menu).pack(pady=10)

# ---------------- 3. TIC TAC TOE ----------------
def tic_tac_toe():
    clear()

    board = [" "] * 9
    turn = ["X"]

    tk.Label(root, text="❌⭕ TIC TAC TOE",
             bg="#1e1e2e", fg="white",
             font=("Arial", 14)).pack()

    frame = tk.Frame(root, bg="#1e1e2e")
    frame.pack()

    result = tk.Label(root, text="", bg="#1e1e2e", fg="yellow")
    result.pack()

    def check_win():
        combos = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a,b,c in combos:
            if board[a] == board[b] == board[c] != " ":
                return board[a]
        return None

    def click(i):
        if board[i] == " ":
            board[i] = turn[0]
            buttons[i].config(text=turn[0])

            winner = check_win()
            if winner:
                result.config(text=f"🎉 {winner} Wins!")
                return

            turn[0] = "O" if turn[0] == "X" else "X"

    buttons = []
    for i in range(9):
        b = tk.Button(frame, text=" ", width=5, height=2,
                      command=lambda i=i: click(i))
        b.grid(row=i//3, column=i%3)
        buttons.append(b)

    tk.Button(root, text="⬅ Back", command=main_menu).pack(pady=10)

# ---------------- START ----------------
main_menu()
root.mainloop()