# Maintainer: Kevin Phan, kevin2006phan@gmail.com
pkgname=wallpaper-cli
pkgver=1.0
pkgrel=1
pkgdesc="A CLI tool to manipulate SWWW"
arch=('any')
url="https://github.com/Akihiro120/wallpaper-cli"
license=('GPL')
depends=('python' 'swww')

package() {
    install -d "$pkgdir/usr/bin"
    cp -r "$srcdir/"* "$pkgdir/usr/bin/"
    chmod 755 "$pkgdir/usr/bin/"*
    mv "$pkgdir/usr/bin/wallpaper-cli.py" "$pkgdir/usr/bin/wallpaper-cli"
    mv "$pkgdir/usr/bin/wallpaper-cli-cycle.py" "$pkgdir/usr/bin/wallpaper-cli-cycle"
}

