const { watch, src, dest, parallel } = require('gulp')
const sass = require('gulp-sass')
const pug = require('gulp-pug')
const browserify = require('gulp-browserify')
const image = require('gulp-image')

const data = require('./src/json/games.json')


function html (cb) {
    src('src/pug/*.pug')
    .pipe(pug({
        data: { title: 'TGEE', games: data},
        pretty: true
        
    }).on('error', console.log))
    .pipe(dest('./dist'))
    cb()
}

function css(cb) {
    src('./src/scss/index.scss')
    .pipe(sass({
        includePaths: ['node_modules/bootstrap/scss/', 'node_modules/bootstrap/scss/']
    }).on('error', sass.logError))
    .pipe(dest('./dist'))
    cb()
}

function javascript (cb) {
    src('./src/javascript/index.js')
    .pipe(browserify())
    .on('error', console.log)
    .pipe(dest('./dist'))
    cb()
}

function copyAssets (cb) {
    src('./src/images/**/*.{png,gif,jpg}')
    // .pipe(image())
    .pipe(dest('./dist/images'))

    src('./vendor/*')
    .pipe(dest('./dist/vendor'))
    cb()
}


exports.default = function () {
    watch('src/javascript/*.js', javascript)
    watch(['src/scss/*.scss', 'src/**/*.scss'], css)
    watch(['src/pug/*.pug', 'src/pug/**/*.pug'], html)
}

exports.build = parallel(html, css, javascript, copyAssets)