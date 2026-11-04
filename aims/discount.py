def calculate_discounted_total(total, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")

    return total * (1 - percent / 100)