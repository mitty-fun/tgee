const { parallel, src, dest, watch } = require('gulp');
const sass = require('gulp-sass');
const pug = require('gulp-pug');
const webserver = require('gulp-webserver');
const browserify = require('gulp-browserify');

sass.compiler = require('node-sass');

function html() {
  return src('src/pug/*.pug')
    .pipe(pug())
    .pipe(dest('dist/'));
}

function javascript() {
  return src('src/js/*.js')
    .pipe(browserify())
    .pipe(dest('dist/js/'));
}

function css() {
  return src('src/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(dest('dist/css/'));
}

function server() {
  return src('./')
    .pipe(webserver({
      livereload: true,
      directoryListing: true,
      open: true
    }));
};

function copyAssets () {
  return src('./static/*')
    .pipe(dest('dist/static/'))

}
exports.default = function() {
  
  watch('src/js/*.js', javascript);
  watch('src/scss/*.scss', css);
  watch(['src/pug/*.pug', 'src/pug/*/*.pug'], html);

  parallel(html, javascript, css, server, copyAssets)();
};