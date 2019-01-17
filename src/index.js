import 'bootstrap';
import './main.scss';

var pdfjsLib = require('pdfjs-dist');

var pdfPath = '../arxiv.pdf';

// Setting worker path to worker bundle.
pdfjsLib.GlobalWorkerOptions.workerSrc =
  '../dist/pdf.worker.js';

// Loading a document.
var loadingTask = pdfjsLib.getDocument(pdfPath);
loadingTask.promise.then(function (pdfDocument) {
  // Request a first page
  return pdfDocument.getPage(1).then(function (pdfPage) {
    // Display page on the existing canvas with 100% scale.
    var viewport = pdfPage.getViewport(1.5);
    var canvas = document.getElementById('theCanvas');
    canvas.width = viewport.width;
    canvas.height = viewport.height;
    var ctx = canvas.getContext('2d');
    var renderTask = pdfPage.render({
      canvasContext: ctx,
      viewport: viewport,
    });
    return renderTask.promise;
  });
}).catch(function (reason) {
  console.error('Error: ' + reason);
});
