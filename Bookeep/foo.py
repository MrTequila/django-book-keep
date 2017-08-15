import matplotlib
import matplotlib.pyplot as plt


def generate_image(x, y):
    matplotlib.style.use('ggplot')
    plt.bar(x, y, tick_label= x, align = 'center')
    plt.xlabel('months')
    plt.ylabel('time read')
    plt.savefig('E:\Django\BearLynx\Bookeep\static\Bookeep\img\\foo.png')
