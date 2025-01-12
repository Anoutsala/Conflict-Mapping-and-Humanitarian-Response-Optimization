# Conflict Mapping and Humanitarian Response Optimization

## Overview

This project was developed for the Doctors Without Borders (DWB) track as part of the 6th Annual Datathon for Social Good at UC Berkeley, focusing on conflict mapping and humanitarian response optimization. Using the [Armed Conflict Location and Event Data](https://acleddata.com/) (ACLED) dataset from 2018 to 2024, we aimed to create a comprehensive, data-driven solution to assist DWB in making informed decisions about the placement and movement of humanitarian workers. Our work integrates geospatial data, predictive analytics, and machine learning to enhance early warning systems, optimize resource allocation, and prioritize worker safety in volatile environments.

## Objectives
- **Anticipatory Action:** Leverage ML models to predict areas at risk of increased conflict using historical and real-time ACLED data.
- **Conflict Mapping:** Visualize real-time and predictive data to create dynamic maps of potential conflict zones.
- **Risk Assessment for Worker Placement:** Identify safe regions for deployment and highlight areas requiring caution to support DWB's strategic planning.
- **Data-Driven Early Warning System:** Build a robust system to provide timely insights into conflict escalation, enabling proactive resource distribution.

## Real-Time Interactive Maps
- **[Monthly Conflict Events](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/monthly_conflict_events.html)**: A choropleth map showing the intensity of conflict events by country over time, with an animation slider for exploring monthly changes.
- **[Conflict Density Overtime](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/conflict_density.html)**: A density map aggregating conflict intensity into grid cells, visualizing global conflict hotspots across months.
- **[Monthly Fatalities Density Overtime](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/monthly_fatalities.html)**: A choropleth map illustrating fatalities by country over time, highlighting regions most affected each month.
- **[Fatality Density Over Time](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/fatality_density.html)**: A density map aggregating fatality counts into grid cells, providing insights into the spatial distribution of fatal events over time.
- **[Percentage Change in Monthly Conflict Events](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/percent_change_events.html)**: A choropleth map showing the percentage change in conflict events by country over time, with a color gradient indicating decreases (blue) and increases (red).
- **[Percentage Change in Monthly Fatalities by Country and Year](https://anoutsala.github.io/Conflict-Mapping-and-Humanitarian-Response-Optimization/conflict_visualizations/percent_change_fatalities.html)**: A choropleth map illustrating the percentage change in fatalities by country over time, with a color gradient highlighting decreases (blue) and increases (red).

## Findings
### Markov models
![Markov models](next_most_likely_actor.png)
- **Actor Transition Probabilities:** We calculated the likelihood of transitions between actors in conflict events, revealing patterns of collaboration or succession within countries.  
- **Predictive Insights:** The model identifies the most likely next actors in conflict sequences, providing actionable predictions for future events.
#### Implications
- **Resource Allocation:** Anticipating high-probability transitions aids in more effective deployment of resources and interventions.  
- **Strategic Planning:** Understanding actor dynamics supports tailored strategies to address conflict patterns.
