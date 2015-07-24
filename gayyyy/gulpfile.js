// Include gulp
var gulp = require('gulp');
var connect = require('gulp-connect')

// Include Our Plugins
var jshint = require('gulp-jshint');

// Lint Task
gulp.task('lint', function() {
    return gulp.src('./js/*.js')
        .pipe(jshint())
        .pipe(jshint.reporter('default'));
});

// Watch Files For Changes
gulp.task('watch', function() {
    gulp.watch(['./front/src/**/*.js'], ['js']);
    gulp.watch(['./front/src/*.html'], ['html']);
});


gulp.task('html', function() {
    gulp.src('./front/src/*.html')
    .pipe(connect.reload());
});

gulp.task('js', function() {
    gulp.src('./front/src/**/*.js')
    .pipe(connect.reload());
});

gulp.task('connect', function() {
    connect.server({
        root: '.',
        livereload: true,
        port: 8081
    });
});

gulp.task('default', 'watch');
