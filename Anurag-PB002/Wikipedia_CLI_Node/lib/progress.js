function Progress() {
    this.stream = process.stderr;
    this.loading = undefined;
    this.index = 0;
    this.progressMessage = 'Loading';
    this.pieces = [
        '- ' + this.progressMessage + '.',
        '\\ ' + this.progressMessage + '..',
        '| ' + this.progressMessage + '...',
        '/ ' + this.progressMessage + '....'
    ];
}

Progress.prototype = {
    start: function () {
        var self = this;

        this.loading = setInterval(function () {
            self.stream.clearLine();
            self.stream.write(self.pieces[self.index++]);
            self.stream.cursorTo(0);

            if (self.index > 3) {
                self.index = 0;
            }
        }, 150);
    },

    setProgressMessage: function (message) {
        this.progressMessage = message;
    },

    finish: function () {
        this.stream.clearLine();
        clearInterval(this.loading);
    }

};

module.exports = Progress;
