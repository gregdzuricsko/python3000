'use strict';

var browserify = require('browserify');
var gulp = require('gulp');
var source = require('vinyl-source-stream');
var react = require('reactify');
var watchify = require('watchify');
var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
var uglify = require('gulp-uglify');
var streamify = require('gulp-streamify');
var htmlreplace = require('gulp-html-replace')


var path = {
  HTML: 'src/index.html',
  MINIFIED_OUT: 'build.min.js',
  OUT: 'build.js',
  DEST: 'dist',
  DEST_BUILD: './dist/build',
  DEST_SRC: './dist/src',
  ENTRY_POINT: './src/js/app.js'
};


//basic browserify build with reactify transform
gulp.task('build', function () {
  // set up the browserify instance on a task basis
  browserify({
    entries: path.ENTRY_POINT,
    transform: [react]
  })
    .bundle()
    .pipe(source(path.MINIFIED_OUT))
    .pipe(streamify(uglify(path.MINIFIED_OUT)))
    .pipe(gulp.dest(path.DEST_BUILD));
});


//watch with browserify and reactify
gulp.task('watch', function() {
  gulp.watch(path.HTML, ['copy']);

  var watcher  = watchify(browserify({
    entries: [path.ENTRY_POINT],
    transform: [react],
    debug: true,
    cache: {}, packageCache: {}, fullPaths: true
  }));

  return watcher.on('update', function () {
    watcher.bundle()
      .pipe(source(path.OUT))
      .pipe(gulp.dest(path.DEST_SRC));
      console.log('Updated');
  })
    .bundle()
    .pipe(source(path.OUT))
    .pipe(gulp.dest(path.DEST_SRC));
});

gulp.task('replaceHTML', function(){
  gulp.src(path.HTML)
    .pipe(htmlreplace({
      'js': 'build/' + path.MINIFIED_OUT
    }))
    .pipe(gulp.dest(path.DEST));
});

gulp.task('copy', function(){
  gulp.src(path.HTML)
    .pipe(gulp.dest(path.DEST));
});


//we want to lint our source files, not the browserified ones 
gulp.task('lint', function() {
return gulp.src('./src/**/*.js')
  .pipe(jshint())
  .pipe(jshint.reporter(stylish));
});

gulp.task('production', ['replaceHTML', 'build']);
gulp.task('default', ['copy','lint','watch']);
