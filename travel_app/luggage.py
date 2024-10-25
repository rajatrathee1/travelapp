def suggest_luggage(journey):
    # Basic items everyone should pack
    base_items = ['Passport', 'Tickets', 'Wallet', 'Phone Charger']

    # Suggested items based on journey type
    if journey.journey_type == 'business':
        items = base_items + [
            'Business Attire',
            'Laptop',
            'Notebook',
            'Formal Shoes',
        ]
    elif journey.journey_type == 'vacation':
        items = base_items + [
            'Casual Wear',
            'Sunglasses',
            'Camera',
            'Swimwear',
        ]
    elif journey.journey_type == 'adventure':
        items = base_items + [
            'Hiking Boots',
            'Backpack',
            'First Aid Kit',
            'Flashlight',
        ]
    else:
        items = base_items + ['Basic Clothing']

    # Adjust items based on duration
    extra_clothes = ['Extra Set of Clothes'] * (journey.duration // 3)
    items.extend(extra_clothes)

    return items
