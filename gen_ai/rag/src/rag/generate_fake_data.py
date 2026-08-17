from reportlab.lib.pagesizes import A4  # physical dimensions of pdf
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    Paragraph,
    Spacer,
    Table,
    SimpleDocTemplate,
    PageBreak,
    TableStyle,
)
from reportlab.lib import colors
from pathlib import Path


def generate_fake_data(output_path: Path):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=54,
        leftMargin=54,
        topMargin=54,
        bottomMargin=54,
        title="Aegis Dynamics Corporation: 50-Year Operational & Financial Archive (1976–2026)",
        author="Aegis Dynamics Corporation",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Heading1"],
        fontSize=24,
        leading=28,
        spaceAfter=20,
        textColor=colors.HexColor("#1A237E"),
    )

    h1_style = ParagraphStyle(
        "YearHeading",
        parent=styles["Heading2"],
        fontSize=16,
        leading=20,
        spaceBefore=15,
        spaceAfter=10,
        textColor=colors.HexColor("#0D47A1"),
    )

    body_style = ParagraphStyle(
        "Body", parent=styles["Normal"], fontSize=10, leading=14, spaceAfter=8
    )

    story = []

    story.append(
        Paragraph(
            "Aegis Dynamics Corporation: 50-Year Operational & Financial Archive (1976–2026)",
            title_style,
        )
    )

    story.append(
        Paragraph(
            "<b>Classification:</b> Internal Historical & Policy Record", body_style
        )
    )

    story.append(
        Paragraph(
            "This master document contains the complete historical filings, corporate governance changes, "
            "annual financial statements, employee handbooks, and operational memos for Aegis Dynamics Corporation "
            "from its founding in March 1976 through the Q2 2026 reporting period.",
            body_style,
        )
    )

    story.append(Spacer(1, 15))
    story.append(PageBreak())

    ceos = [
        (1976, 1989, "Arthur Vance Pendelton", "Founding & Industrial Automation"),
        (1990, 2004, "Eleanor Vance-Sterling", "Expansion & Digital Logistics"),
        (2005, 2017, "Marcus Thorne", "Cloud Migration & Global Restructuring"),
        (2018, 2026, "Dr. Seraphina Chen", "Autonomous Systems & Edge AI"),
    ]

    hq_locations = [
        (1976, 1995, "Akron, Ohio (Plant No. 1)"),
        (1996, 2011, "Chicago, Illinois (Michigan Avenue Center)"),
        (2012, 2026, "Austin, Texas (Silicon Hills Campus)"),
    ]

    for year in range(1976, 2027):

        current_ceo = next(c[2] for c in ceos if c[0] <= year <= c[1])
        current_focus = next(c[3] for c in ceos if c[0] <= year <= c[1])
        current_hq = next(h[2] for h in hq_locations if h[0] <= year <= h[1])

        base_revenue = 1.2 * ((year - 1975) ** 1.85)
        operating_expense = base_revenue * 0.68
        net_profit = base_revenue - operating_expense
        headcount = int(45 * ((year - 1975) ** 1.25))

        story.append(
            Paragraph(
                f"Section {year - 1975}: Annual Report & Governance Record — {year}",
                h1_style,
            )
        )
        story.append(
            Paragraph(
                f"<b>Executive Leadership:</b> Chief Executive Officer: {current_ceo} | Strategic Priority: {current_focus}",
                body_style,
            )
        )
        story.append(
            Paragraph(
                f"<b>Primary Operational Headquarters:</b> {current_hq}", body_style
            )
        )
        story.append(
            Paragraph(
                f"<b>Active Global Headcount:</b> {headcount:,} full-time equivalents.",
                body_style,
            )
        )
        story.append(Spacer(1, 6))

        story.append(
            Paragraph(
                f"During the fiscal year {year}, Aegis Dynamics executed several operational initiatives under the leadership of {current_ceo}. "
                f"Capital expenditure for the fiscal period centered on expanding manufacturing capabilities aligned with {current_focus.lower()}. "
                f"Compliance audits confirmed adherence to internal standard protocol <b>AD-POL-{year % 100:02d}B</b>.",
                body_style,
            )
        )

        if year == 1983:
            story.append(
                Paragraph(
                    "<b>Policy Directive (1983-04):</b> Strict prohibition against personal computing devices within server rooms. All mainframe access must be authorized using dual physical security keys.",
                    body_style,
                )
            )
        elif year == 1999:
            story.append(
                Paragraph(
                    "<b>Y2K Readiness Memo (1999-11):</b> Legacy COBOL databases for payroll migrated to Oracle SQL. Contingency backup tapes archived off-site in Boulder, Colorado.",
                    body_style,
                )
            )
        elif year == 2008:
            story.append(
                Paragraph(
                    "<b>Global Crisis Restructuring (2008-09):</b> Travel budget reduced by 40%. Flexible work arrangements introduced allowing Friday remote work for engineering staff.",
                    body_style,
                )
            )
        elif year == 2020:
            story.append(
                Paragraph(
                    "<b>Emergency Remote Policy (2020-03):</b> 100% remote work mandate enacted across all non-manufacturing personnel. VPN encryption updated to AES-256 with mandatory hardware security keys.",
                    body_style,
                )
            )
        elif year == 2024:
            story.append(
                Paragraph(
                    "<b>Project Boreas Authorization (2024-08):</b> Allocation of $42.5M for the development of the Boreas edge-computing drone array for agricultural monitoring.",
                    body_style,
                )
            )

        table_data = [
            ["Metric", "Fiscal Year Value (USD)"],
            ["Gross Revenue", f"${base_revenue:,.2f} M"],
            ["Operating Expenses", f"${operating_expense:,.2f} M"],
            ["Net Income", f"${net_profit:,.2f} M"],
            [
                "Auditing Firm",
                "Kensington & Finch LLP" if year < 2002 else "Deloitte & Touche",
            ],
        ]

        t = Table(table_data, colWidths=[180, 220])

        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EAF6")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#1A237E")),
                    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("FONTSIZE", (0, 0), (-1, -1), 9),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B0BEC5")),
                ]
            )
        )

        story.append(t)
        story.append(Spacer(1, 10))

        if year % 2 == 0:
            story.append(PageBreak())

    doc.build(story)
    print("✅ Generated fake massive PDF: report.pdf")
