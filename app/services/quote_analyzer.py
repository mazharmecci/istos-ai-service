def analyze_quote(payload):
    quote = payload.quote
    historical = payload.historical_context

    win_probability = 85 if quote.deal_value <= historical.avg_winning_price * 1.2 else 60
    pricing_risk = "Low" if win_probability >= 80 else "Medium"

    risks = [
        f"Quoted value ₹{quote.deal_value} vs historical avg ₹{historical.avg_winning_price}",
        f"{quote.hospital} is moderately price sensitive"
    ]

    return {
        "win_probability": win_probability,
        "pricing_risk": pricing_risk,
        "key_risks": risks,
        "recommended_focus": (
            "Emphasize service reliability and long-term support rather than price discounts"
        )
    }
