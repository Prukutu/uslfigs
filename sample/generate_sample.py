import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import numpy as np

plt.style.use('usl-presentations')
x = np.arange(0, 180, 1)
y = np.sin(x*np.pi/180)

fig, ax = plt.subplots()
ax.plot(x, y, label='test1')
ax.plot(x, y - .1, label='test2')
ax.plot(x, y - .2, label='test3')
# path = '/usr/share/fonts/opentype/IBM Plex Sans/IBM_Plex_Sans_Text.otf'
# prop = font_manager.FontProperties(path)

ax.set_title('This is my plot', loc='left')
             # fontname='IBM Plex Sans',
             # fontweight='medium',
             # fontsize=24)

ax.set_xlabel(u'X-Axis \u00b0F')
ax.set_ylabel('Y-Axis')
ax.legend()
plt.show()
fig.savefig('test.png')
