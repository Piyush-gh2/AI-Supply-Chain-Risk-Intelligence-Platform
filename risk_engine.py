def detect_risk(inventory, delay):

    if inventory < 100:
        return "Critical Inventory Alert"

    elif delay == 1:
        return "Supplier Delay Risk"

    else:
        return "Supply Chain Stable"