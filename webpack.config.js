var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')

config.devtool = "#eval-source-map"

config.plugins = config.plugins.concat([
  new BundleTracker({filename: './webpack-stats-local.json'}),
])

config.module.loaders.push(
  { test: /\.jsx?$/, exclude: /node_modules/, loaders: ['react-hot', 'babel'] }
)

config.module.loaders.push(
  { test: /\.css$/, loader: "style-loader" })

config.module.loaders.push(
  {
  test: /\.css$/,
  loader: 'css-loader',
  query: {
    modules: true,
    localIdentName: '[name]__[local]___[hash:base64:5]'
  }
})

config.module.loaders.push(
{
  test: /\.(jpg|png)$/,
  loader: 'url?limit=10000&publicPath=./static/bundles/local/&name=[name].[ext]'
})

module.exports = config