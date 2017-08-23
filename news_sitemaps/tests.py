from django.test import TestCase


class NewsSitemapsTests(TestCase):
    def test_index(self):
        resp = self.client.get('/news-sitemaps/index.xml')
        
        self.assertEqual(resp.content, '<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">\n\t<sitemap><loc>https://example.com/news-sitemaps/comments.xml</loc></sitemap>\n\n</sitemapindex>')
        
    def test_comments(self):
        resp = self.client.get('/news-sitemaps/comments.xml')
        
        self.assertEqual(resp.content, '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9"\n        xmlns:n="https://www.google.com/schemas/sitemap-news/0.9">\n\t\n</urlset>')
