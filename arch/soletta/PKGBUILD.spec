pkgname=soletta
pkgver=1_beta7
pkgrel=1
checkdepends=()
conflicts=('soletta-git')
source=("https://github.com/solettaproject/soletta/archive/v$pkgver.tar.gz"
        "https://github.com/solettaproject/duktape-release/archive/v1_beta2.tar.gz"
        "https://codeload.github.com/01org/tinycbor/tar.gz/f0791a2a12599c82e9b65f2923eb1cdd6c141e5d")
md5sums=('f5b87201c8bbf78f49bef2c81b3bf049'
         '69195d623d739158ecb055aeb02fd77b'
         '5ebd7c2a5f092a1a6ef0704d6121ae04')

prepare() {
    cp -r duktape-release-1_beta2/* "$pkgname-$pkgver"/src/thirdparty/duktape/
    cp -r tinycbor-f0791a2a12599c82e9b65f2923eb1cdd6c141e5d/* "$pkgname-$pkgver"/src/thirdparty/tinycbor/
}

build() {
	cd "$pkgname-$pkgver"
    make alldefconfig
	make
}

package() {
	cd "$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
