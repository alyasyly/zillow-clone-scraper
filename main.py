from scraper import get_data
from form_filler import fill_form

def main():
    data = get_data()
    fill_form(data)    


if __name__ == "__main__":
    main()
