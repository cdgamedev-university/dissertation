library(ggplot2)

metrics <- read.csv("metrics.csv")

sample <- subset(metrics, algorithm == "mean_sd")

p <-
  ggplot(sample, aes(x = gemID, y = dataSize, fill = factor(gemID))) +
  geom_bar(stat="identity") +
  geom_text(aes(label = dataSize), nudge_y = sample$dataSize * -0.5) +
  labs(x = "Gem ID", y = "Count") +
  coord_cartesian(expand = FALSE, xlim = c(NA, NA), ylim = c(0, 1000)) +
  scale_y_continuous(breaks=seq(0, 1000, 100)) +
  theme(legend.position = "none", plot.title = element_text(hjust = 0.5))

print(p)