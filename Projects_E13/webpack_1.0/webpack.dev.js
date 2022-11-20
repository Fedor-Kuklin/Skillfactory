const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = merge(common, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    static: './dist',
    open: true,
    compress: true,
    hot: true,
    port: 8080,
    stats: {
      children: false,
      maxModules:0
    }
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.js$/,
        exclude: '/node_modules',
        use: ['eslint-loader'],
      }
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      meta: {
            'viewport': 'width=device-width, initial-scale=1, shrink-to-fit=no',
      },
      title: 'Development',
    }),
    
  ],
  optimization: {
    runtimeChunk: 'single',
  },
});