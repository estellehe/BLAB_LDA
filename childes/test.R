library(tidyverse)

data <- read_csv("wiki_file_100_animal.csv")
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
  gather(`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, 
         `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, 
         `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, 
         `31`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, 
         `41`, `42`, `43`, `44`, `45`, `46`, `47`, `48`, `49`, `50`, 
         `51`, `52`, `53`, `54`, `55`, `56`, `57`, `58`, `59`, `60`, 
         `61`, `62`, `63`, `64`, `65`, `66`, `67`, `68`, `69`, `70`, 
         `71`, `72`, `73`, `74`, `75`, `76`, `77`, `78`, `79`, `80`, 
         `81`, `82`, `83`, `84`, `85`, `86`, `87`, `88`, `89`, `90`, 
         `91`, `92`, `93`, `94`, `95`, `96`, `97`, `98`, `99`, 
         key = 'topic', value = 'wcountlg')

ggplot(data = result) + 
  geom_bar(mapping = aes(x = wcountlg, fill = topic), position = "dodge") + 
  labs(
    title = "Animal MCDI Words Probability Distribution in wiki_100",
    x = "lg(word probability)",
    y = "word count")

