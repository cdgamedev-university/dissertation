library(ggplot2)

metrics <- read.csv("time-metrics.csv")
metrics$algorithm <- factor(metrics$algorithm, levels = c("CleverSD", "2T", "Median", "Mean"))

p <-
  ggplot(metrics, aes(x = algorithm, y = (time / dataSize) * 1000)) +
  geom_bar(aes(fill = algorithm), position="dodge", stat="identity") +
  labs(x = "Algorithm", y = "Average Time Taken per 1000 Elements (ms)", color = "Algorithm") +
  coord_cartesian(expand = FALSE, xlim = c(NA, NA), ylim = c(0, 17.5)) +
  scale_y_continuous(breaks=seq(0, 17.5, 2.5)) +
  theme(legend.position = "none", plot.title = element_text(hjust = 0.5))

print(p)