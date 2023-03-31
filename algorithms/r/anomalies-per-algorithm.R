library(ggplot2)

metrics <- read.csv("metrics.csv")
metrics$algorithm <- factor(metrics$algorithm, levels = c("clever_sd", "twostage_sd", "median_sd", "mean_sd"))

p <-
  ggplot(metrics, aes(x = gemID, y = (anomalies / dataSize) * 100, group = algorithm)) +
  scale_color_manual(values = c("red", "orange", "green", "blue")) +
  geom_bar(aes(fill = algorithm), position="dodge", stat="identity") +
  labs(x = "Gem ID", y = "Anomalies per Gem (%)", color = "Algorithm") +
  coord_cartesian(expand = FALSE, xlim = c(NA, NA), ylim = c(0, 60)) +
  theme(plot.title = element_text(hjust = 0.5)) +
  scale_y_continuous(breaks=seq(0, 60, 10))

print(p)