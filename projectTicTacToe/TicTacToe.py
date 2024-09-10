import tkinter as tk
from tkinter import messagebox


class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        # Variáveis para controlar o estado do jogo
        self.jogador_atual = "X"
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]
        self.vitorias_X = 0
        self.vitorias_O = 0
        self.limite_vitorias = 3  # Limite de vitórias para reiniciar o jogo e zerar o placar

        # Contadores de vitórias
        self.label_vitorias_X = tk.Label(self.root, text=f"Vitórias X: {self.vitorias_X}")
        self.label_vitorias_X.grid(row=0, column=0)
        self.label_vitorias_O = tk.Label(self.root, text=f"Vitórias O: {self.vitorias_O}")
        self.label_vitorias_O.grid(row=0, column=2)

        # Botão para reiniciar o jogo
        self.botao_reiniciar = tk.Button(self.root, text="Start", command=self.reiniciar_jogo)
        self.botao_reiniciar.grid(row=0, column=1)

        # Criar botões para o tabuleiro
        self.criar_tabuleiro()

    def criar_tabuleiro(self):
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                botao = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda i=i, j=j: self.marcar(i, j))
                botao.grid(row=i + 1, column=j)
                self.botoes[i][j] = botao

    def marcar(self, i, j):
        if not self.botoes[i][j]["text"]:  # Verifica se a célula está vazia
            self.botoes[i][j]["text"] = self.jogador_atual
            self.tabuleiro[i][j] = self.jogador_atual

            # Define a cor do botão
            if self.jogador_atual == "X":
                self.botoes[i][j]["bg"] = "red"
            else:
                self.botoes[i][j]["bg"] = "yellow"

            # Verifica se há um vencedor
            if self.verificar_vitoria():
                self.finalizar_jogo(vencedor=self.jogador_atual)
            elif self.verificar_empate():
                self.finalizar_jogo(vencedor=None)
            else:
                # Alterna o jogador
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"

    def verificar_vitoria(self):
        # Verificar linhas, colunas e diagonais
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] and self.tabuleiro[i][0]:
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] and self.tabuleiro[0][i]:
                return True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] and self.tabuleiro[0][0]:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] and self.tabuleiro[0][2]:
            return True

        return False

    def verificar_empate(self):
        # Verifica se todas as células estão preenchidas
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] is None:
                    return False
        return True

    def finalizar_jogo(self, vencedor):
        if vencedor:
            messagebox.showinfo("Fim de Jogo", f"O jogador {vencedor} venceu!")
            if vencedor == "X":
                self.vitorias_X += 1
                self.root.configure(bg="red")  # Cor de fundo vermelha
            else:
                self.vitorias_O += 1
                self.root.configure(bg="yellow")  # Cor de fundo amarela
        else:
            messagebox.showinfo("Fim de Jogo", "Empate!")
            self.root.configure(bg="gray")  # Cor de fundo cinza para empate

        # Atualizar o contador de vitórias
        self.label_vitorias_X.config(text=f"Vitórias X: {self.vitorias_X}")
        self.label_vitorias_O.config(text=f"Vitórias O: {self.vitorias_O}")

        # Verificar se algum jogador atingiu o limite de vitórias
        if self.vitorias_X == self.limite_vitorias or self.vitorias_O == self.limite_vitorias:
            messagebox.showinfo("Fim de Jogo", "Um jogador atingiu 3 vitórias. Placar será zerado.")
            self.reiniciar_placar()
        else:
            # Bloquear o tabuleiro
            for i in range(3):
                for j in range(3):
                    self.botoes[i][j]["state"] = "disabled"

    def reiniciar_placar(self):
        # Reiniciar placar de vitórias
        self.vitorias_X = 0
        self.vitorias_O = 0
        self.label_vitorias_X.config(text=f"Vitórias X: {self.vitorias_X}")
        self.label_vitorias_O.config(text=f"Vitórias O: {self.vitorias_O}")
        self.reiniciar_jogo()

    def reiniciar_jogo(self):
        # Limpar o tabuleiro e redefinir as variáveis
        self.jogador_atual = "X"
        self.tabuleiro = [[None for _ in range(3)] for _ in range(3)]
        self.root.configure(bg="SystemButtonFace")  # Restaurar cor original

        # Reinicializar botões
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="", bg="SystemButtonFace", state="normal")


# Inicializar a interface gráfica
root = tk.Tk()
jogo = JogoDaVelha(root)
root.mainloop()
