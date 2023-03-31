library(ggplot2)
library(scales)

data <- read.csv('./Gem Data/all-gems.csv')

p <-
  ggplot(data, aes(x = GemID, y = Cost, fill = factor(GemID))) +
  labs(x = "Gem ID", y = "Gem Cost (Gold)") +
  geom_boxplot(aes(x = GemID, y = Cost)) +
  coord_cartesian(expand = FALSE, xlim = c(NA, NA), ylim = c(0, 1650000)) +
  scale_y_continuous(breaks=seq(0, 1650000, 75000), labels = comma) +
  theme(legend.position = "none", plot.title = element_text(hjust = 0.5))

print(p)