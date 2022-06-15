from howlongtobeatpy import HowLongToBeat


class HowLongToBeatAPIHandler:
    def __init__(self):
        pass


    def fetch_data(self, app_name):
        results = HowLongToBeat().search(app_name)
        if results is not None and len(results) > 0:
            best_element = max(results, key=lambda element: element.similarity)
            return best_element
        else:
            return None
