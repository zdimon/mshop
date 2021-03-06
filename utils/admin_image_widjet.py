# -*- coding: utf-8 -*-
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
import os
from sorl.thumbnail import get_thumbnail

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):

            image_url = value.url
            file_name=str(value)

            # defining the size
            size='100x100'
            x, y = [int(x) for x in size.split('x')]
            try :
                # defining the filename and the miniature filename
                filehead, filetail  = os.path.split(value.path)
                basename, format    = os.path.splitext(filetail)
                miniature           = basename + '_' + size + format
                filename            = value.path
                miniature_filename  = os.path.join(filehead, miniature)
                filehead, filetail  = os.path.split(value.url)
                miniature_url       = filehead + '/' + miniature

                # make sure that the thumbnail is a version of the current original sized image
                if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
                    os.unlink(miniature_filename)

                # if the image wasn't already resized, resize it
                if not os.path.exists(miniature_filename):
                    try:
                        image = get_thumbnail(filename, '130x100', crop='center', quality=99)
                    except NameError:
                        pass
                    #try:
                    #    image.save(miniature_filename, image.format, quality=100, optimize=1)
                    #except:
                    #    image.save(miniature_filename, image.format, quality=100)
                #import pdb; pdb.set_trace()
                output.append(u' <div style="float:right; padding: 10px 20px 10px 300px;"><a href="%s" target="_blank"><img src="%s" alt="%s" /></a></div> %s ' % \
                (value.url, image.url, image.url, u'Изменить:'))
            except TypeError:
                pass
        output.append(u'<div sttyle="float:left">'+super(AdminFileWidget, self).render(name, value, attrs)+u'</div>')
        return mark_safe(u''.join(output))
