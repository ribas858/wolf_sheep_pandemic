# importe o arquivo ".csv"

dataset <- wolfsheep_pandemic_model_data_it_30_steps_150_data_22_08_2022_06_38 # "Arquvio .csv"

# R_comand_1
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0)"); abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_2
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0 & dataset$sheep_reproduce == 0.4] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0, e Tx Reprod. Ov == 0.4)") ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_3
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0 & dataset$sheep_reproduce == 0.8] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0, e Tx Reprod. Ov == 0.8)") ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_4
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0 & dataset$sheep_reproduce == 0.4 & dataset$grass_regrowth_time==30] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0, e Tx Repr.Ov == 0.4, e Temp Cresc. Grama == 30 Steps)", cex.main=0.9) ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_5
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0 & dataset$sheep_reproduce == 0.4 & dataset$grass_regrowth_time==45] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0, e Tx Repr.Ov == 0.4, e Temp Cresc. Grama == 45 Steps)", cex.main=0.9) ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_6
busca <- ( dataset$Ovelhas[dataset$Lobos.Imunes==0 & dataset$Lobos.Comuns==0 & dataset$grass_regrowth_time==45] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( LC e LI: Restantes == 0, e Temp Cresc. Grama == 45 Steps)", cex.main=0.9) ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)

# R_comand_7
busca <- ( dataset$Grama[dataset$Ovelhas == 0] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1]; hist(
    busca, breaks = 100, col = "gray", xlab = "Grama", ylab = "Frequência", main = "Grama Restante : ( Ovelhas Restantes == 0)") ; abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend(
        x="topleft", legend = paste("Média Grama Restante: ", as.character( format(round(media, 2), nsmall = 2) )), col="green", lty=1,
        lwd=2)

# R_comand_8
busca <- ( dataset$Ovelhas[dataset$predator_init_doente==1 & dataset$sheep_reproduce == 0.4 & dataset$grass_regrowth_time==30] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1] ; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( Lobo Doente Inicialmente == 1, e Tx Repr.Ov == 0.4, e Temp Cresc. Grama == 30 Steps)", cex.main=0.8); abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)
# R_comand_9
busca <- ( dataset$Ovelhas[dataset$predator_init_doente==6 & dataset$sheep_reproduce == 0.5 & dataset$grass_regrowth_time==35] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1] ; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( Lobo Doente Inicialmente == 6, e Tx Repr.Ov == 0.5, e Temp Cresc. Grama == 35 Steps)", cex.main=0.8); abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)
# R_comand_10
busca <- ( dataset$Ovelhas[dataset$predator_init_doente==8 & dataset$sheep_reproduce == 0.4 & dataset$grass_regrowth_time==45] ); media <-
  mean(busca); total <- length(busca) * dataset$initial_sheep[1] ; mediaPercent <-(media * 100) / total; hist(
    busca, breaks = 100, col = "gray", xlab = "Ovelhas", ylab = "Frequência", main = "Ovelhas Restantes : ( Lobo Doente Inicialmente == 8, e Tx Repr.Ov == 0.4, e Temp Cresc. Grama == 45 Steps)", cex.main=0.8); abline(
      v = mean(dataset$Ovelhas[dataset$predator_init_doente==1]), col = "green", lwd = 2); legend( title = paste("Experimentos Pareados: ", length(busca)), title.col = "blue", title.adj = 0.5,
                                                                                                   x="topright", legend = paste("Média de Ovelhas Restantes: ", as.character( format(round(media, 2), nsmall = 2) ),
                                                                                                                                " (", as.character( format(round(mediaPercent, 6), nsmall = 6)), " %)" ), col="green", lty=1,
                                                                                                   lwd=2)
