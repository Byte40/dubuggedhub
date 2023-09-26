const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass')); // Specify 'sass' as the Sass compiler
const autoprefixer = require('gulp-autoprefixer');

function compileSass() {
   return gulp.src('src/scss/*.scss')
       .pipe(sass().on('error', sass.logError))
       .pipe(autoprefixer())
       .pipe(gulp.dest('dist/css'));
}

function watch() {
   gulp.watch('src/scss/*.scss', compileSass);
}

exports.default = gulp.series(compileSass, watch);
