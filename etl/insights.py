def generate_weekly_summary(prod_score, sleep_index, ratio):
    lines = []

    if prod_score > 70:
        lines.append("Good productivity this week.")
    else:
        lines.append("Productivity was low. Reduce distractions.")

    if sleep_index > 80:
        lines.append("Sleep patterns look healthy.")
    else:
        lines.append("Sleep duration insufficient. Try going to bed early.")

    if ratio > 1:
        lines.append("Entertainment time exceeded work time.")
    else:
        lines.append("Balanced work and entertainment usage.")

    return " ".join(lines)
