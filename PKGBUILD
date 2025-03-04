# Maintainer: Kevin Phan, kevin2006phan@gmail.com
pkgname=hyprpaper-cli
pkgver=1.0
pkgrel=1
pkgdesc="A CLI tool to manipulate Hyprpaper"
arch=('any')
depends=('python' 'hyprpaper')
source=("hyprpaper-cli.py")
md5sums=('SKIP')

package() {
    install -Dm755 "${srcdir}/hyprpaper-cli.py" "${pkgdir}/usr/bin/hyprpaper-cli"
}
