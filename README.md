# Nigeria Property Centre Property Scraper

A Python-based web scraper for extracting property listing information and gallery images from Nigeria Property Centre (NPC).

The project combines web scraping, HTML parsing, regular expressions, JSON extraction, HTTP requests, and OpenCV image processing to automate the collection of property listing data.

## Features

* Extracts property ID
* Extracts property title
* Extracts property price
* Extracts property location
* Extracts date posted
* Extracts contact phone number
* Extracts the full property description
* Extracts rental and financial information
* Detects service charges and additional fees
* Extracts property gallery images
* Downloads property images automatically
* Converts WebP images to JPEG
* Saves processed images to a specified local folder
* Provides a summary of the scraping results

## Technologies Used

* **Python**
* **Requests** — HTTP requests and downloading web content
* **BeautifulSoup** — HTML parsing and data extraction
* **Regular Expressions (Regex)** — Pattern matching and extracting structured information
* **JSON** — Processing embedded gallery data
* **OpenCV** — Image processing and WebP-to-JPEG conversion

## How It Works

The scraper follows this workflow:

```text
NPC Property Listing
        ↓
   HTTP Request
        ↓
    HTML Page
        ↓
 BeautifulSoup Parsing
        ↓
Property Data Extraction
        ↓
Gallery JSON Extraction
        ↓
   Image Download
        ↓
OpenCV Processing
        ↓
 WebP → JPEG
        ↓
 Local Storage
```

## Data Extracted

The scraper currently extracts the following information:

| Field           | Description                     |
| --------------- | ------------------------------- |
| Property ID     | Unique NPC property identifier  |
| Title           | Property listing title          |
| Price           | Advertised property price       |
| Location        | Property location               |
| Date Posted     | Listing publication date        |
| Phone           | Advertised contact number       |
| URL             | Original property listing URL   |
| Description     | Full property description       |
| Rent            | Rental amount where available   |
| Service Charge  | Service charge where available  |
| Legal & Agency  | Legal and agency charges        |
| Caution Deposit | Caution deposit where available |
| Inspection Fee  | Inspection fee where available  |
| Gallery         | Property listing images         |

## Example Use Case

This project can be used as a starting point for real-estate data collection and analysis.

For example, a property professional could use it to collect structured information from property listings for:

* Market research
* Property price analysis
* Listing comparisons
* Real-estate market monitoring
* Property marketing research
* Building a property database
* Image collection and processing
* Automated property research workflows

## Installation

Clone the repository:

```bash
git clone https://github.com/richardoyom/nigeria-property-centre-scraper.git
cd nigeria-property-centre-scraper
```

Install the required Python packages:

```bash
pip install requests beautifulsoup4 opencv-python
```

## Configuration

Update the property URL and local save folder in the Python script:

```python
url = "YOUR_NPC_PROPERTY_URL"

save_folder = r"C:\Users\YOUR_USERNAME\Downloads\property_images"
```

The scraper automatically creates the specified folder if it does not already exist.

## Running the Scraper

Run:

```bash
python scraper.py
```

The program will:

1. Load the property page.
2. Extract the property information.
3. Extract the gallery data.
4. Download the property images.
5. Convert the images to JPEG.
6. Save the processed images locally.
7. Display a scraping summary.

## Example Output

```text
======================================================================
Loading property page...
======================================================================

Searching for gallery images...
Found 12 images.

✅ Saved image_1.jpg
✅ Saved image_2.jpg
✅ Saved image_3.jpg
...

======================================================================
PROPERTY DETAILS
======================================================================

Property ID       : 3621022
Title             : Luxury Furnished 3 Bedroom Apartments
Price             : ...
Location          : Jabi, Abuja
Date Posted       : ...
Phone             : ...
URL               : https://...

DESCRIPTION
----------------------------------------------------------------------

...

FINANCIAL DETAILS
----------------------------------------------------------------------

Rent              : ...
Service Charge    : ...
Legal & Agency    : ...
Caution Deposit   : ...
Inspection Fee    : ...

IMAGE DOWNLOAD SUMMARY
----------------------------------------------------------------------

Images Found      : 12
Converted         : 12
Failed            : 0

======================================================================
SCRAPING COMPLETE
======================================================================
```

## Project Structure

```text
nigeria-property-centre-scraper/
│
├── scraper.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements

A `requirements.txt` file can contain:

```text
requests
beautifulsoup4
opencv-python
```

The `json`, `re`, and `os` modules are part of Python's standard library and do not need to be installed separately.

## Important Note

This project is intended for educational, research, and legitimate real-estate data analysis purposes.

When scraping websites, users should respect the website's terms of service, robots.txt directives, copyright restrictions, rate limits, and applicable laws.

## Future Improvements

Potential improvements include:

* Support for multiple property URLs
* Automatic CSV/Excel export
* Automatic property database storage
* Scraping multiple listings from search pages
* Duplicate image detection
* Automatic image resizing
* Property price analysis
* Location-based market analysis
* Scheduled scraping
* Command-line arguments
* Support for additional Nigerian property websites

## Author

**Richard Oyom**

Property & Construction Project Professional | Estate Surveyor & Valuer

Interested in real-estate technology, property data, web scraping, automation, and digital property platforms.
