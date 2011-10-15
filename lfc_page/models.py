# django imports
from django.utils.translation import ugettext_lazy as _

# lfc imports
import lfc.utils
from lfc.models import BaseContent
from lfc.fields.rich_text import RichTextField

# lfc_page imports
from lfc_page.interfaces import IPage

# zope imports
from zope.interface import implements


class Page(BaseContent):
    """
    A Page displays HTML to the CMS user.

    **Attributes**:

    text:
        The main text of the Page.
    """
    implements(IPage)

    text = RichTextField(_(u"Text"), blank=True)

    def get_searchable_text(self):
        """
        Returns the searchable text of the page. This adds the text to the
        default searchable text.
        """
        searchable_text = self.title + " " + self.description + self.text.text
        return lfc.utils.html2text(searchable_text)

    def edit_form(self, **kwargs):
        """
        Returns the edit form of the page.
        """
        from lfc_page.forms import PageDataForm
        return PageDataForm(**kwargs)
