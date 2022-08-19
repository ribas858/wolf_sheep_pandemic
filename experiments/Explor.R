library(ggplot2)

# importe o arquivo ".csv"

dataset <- wolfsheep_pandemic_model_data_it_2_steps_150_data_18_08_2022_23_37

boxplot(dataset$Ovelhas ~ dataset$Lobos.Comuns, col = "gray", xlab = "Lobos Comuns", ylab = "Ovelhas", main = "Quantidade de Ovelhas X Lobos Comuns")

boxplot(dataset$Ovelhas ~ dataset$Lobos.Doentes, col = "gray", xlab = "Lobos Doentes", ylab = "Ovelhas", main = "Quantidade de Ovelhas X Lobos Doentes")

boxplot(dataset$Ovelhas ~ dataset$Lobos.Doentes, col = "gray", xlab = "Lobos Imunes", ylab = "Ovelhas", main = "Quantidade de Ovelhas X Lobos Imunes")

boxplot(dataset$Lobos.Comuns ~ dataset$Lobos.Doentes, col = "green", xlab = "Lobos Comuns", ylab = "Lobos Doentes", main = "Quantidade de Lobos Comuns X Lobos Doentes")

boxplot(dataset$Lobos.Doentes ~ dataset$Lobos.Imunes, col = "green", xlab = "Lobos Doentes", ylab = "Lobos Imunes", main = "Quantidade de Lobos Doentes X Lobos Imunes")

hist(dataset$Ovelhas, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes")

hist(dataset$Lobos.Comuns, breaks = 100, col = "gray", xlab = "Lobos Comuns", ylab = "Frequência", main = "Lobos Comuns Restantes")

hist(dataset$Lobos.Doentes, breaks = 100, col = "red", xlab = "Lobos Doentes", ylab = "Frequência", main = "Lobos Doentes Restantes")

hist(dataset$Lobos.Imunes, breaks = 100, col = "blue", xlab = "Lobos Imunes", ylab = "Frequência", main = "Lobos Imunes Restantes")

ggplot(data = dataset, mapping = aes(x = Ovelhas, y = Grama)) + 
  geom_point(col = "green")