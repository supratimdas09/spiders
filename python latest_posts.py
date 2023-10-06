import requests
from bs4 import BeautifulSoup

def get_latest_posts_from_upwork():
  """Scrapes the latest posts from Upwork.

  Returns:
    A list of dictionaries, where each dictionary contains the following information about a post:
      * title: The title of the post.
      * description: The description of the post.
      * link: The link to the post.
  """

  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
  }

  response = requests.get('https://www.upwork.com/find-work', headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  posts = []

  for post in soup.find_all('div', class_='job-listing__details'):
    title = post.find('h2', class_='job-listing__title').text
    description = post.find('p', class_='job-listing__description').text
    link = post.find('a', class_='job-listing__link')['href']

    posts.append({
      'title': title,
      'description': description,
      'link': link
    })

  return posts

def get_latest_posts_from_fiverr():
  """Scrapes the latest posts from Fiverr.

  Returns:
    A list of dictionaries, where each dictionary contains the following information about a post:
      * title: The title of the post.
      * description: The description of the post.
      * link: The link to the post.
  """

  headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
  }

  response = requests.get('https://www.fiverr.com/gigs/web-development', headers=headers)

  soup = BeautifulSoup(response.content, 'html.parser')

  posts = []

  for post in soup.find_all('div', class_='gig-card'):
    title = post.find('h2', class_='gig-card__title').text
    description = post.find('p', class_='gig-card__description').text
    link = post.find('a', class_='gig-card__link')['href']

    posts.append({
      'title': title,
      'description': description,
      'link': link
    })

  return posts

if __name__ == '__main__':
  upwork_posts = get_latest_posts_from_upwork()
  fiverr_posts = get_latest_posts_from_fiverr()

  # Combine the posts from Upwork and Fiverr into a single list.
  posts = upwork_posts + fiverr_posts

  # Sort the posts by date, with the most recent posts first.
  posts.sort(key=lambda post: post['date'], reverse=True)

  # Create a report of the latest posts.
  report = ''

  for post in posts:
    report += f'**Title:** {post["title"]}\n'
    report += f'**Description:** {post["description"]}\n'
    report += f'**Link:** {post["link"]}\n\n'

  # Save the report to a file.
  with open('latest_posts.txt', 'w') as f:
    f.write(report)
