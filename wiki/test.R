library(tidyverse)

data <- read_csv("childes_file_25_eta_animal.csv")
tablelist <- list("vector", nrow(data))

for (i in 1:nrow(data)) {
  table <- vector("integer", ncol(data))
  table[[1]] <- data[[1]][[i]]
  for (j in 2:ncol(data)) {
    table[[j]] <- as.integer(log10(data[[j]][[i]]))
  }
  tablelist[[i]] <- table
}

result <- tibble("animal" = 1:(ncol(data)-1))

for (i in 1:length(tablelist)) {
  temp <- tablelist[[i]]
  temp <- temp[2:length(temp)]
  topic <- toString(tablelist[[i]][[1]])
  result <- add_column(result, i = temp)
  colnames(result)[[i+1]] <- topic
}

result <- result %>%
  gather(`0`, `2`, `4`, `6`, `13`, `14`, `20`, `23`, `24`, key = 'topic', value = 'wcountlg')

ggplot(data = result) + 
  geom_bar(mapping = aes(x = wcountlg, fill = topic), position = "dodge")

