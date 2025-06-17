def generate_research_report(topic, questions, answers):
    report_lines = [
        f"# Research Report: {topic}\n",
        f"## Introduction\nThis report provides a comprehensive overview of the topic **{topic}**. It is structured around key questions and supported by recent information gathered from the web.\n"
    ]

    for q in questions:
        report_lines.append(f"## {q}\n")
        report_lines.append(answers.get(q, "No information available."))
        report_lines.append("")

    report_lines.append("## Conclusion\nThis concludes the research. Each question was addressed using live web sources, enabling real-time insights into the topic.\n")

    return "\n".join(report_lines)
