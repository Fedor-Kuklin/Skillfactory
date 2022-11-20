const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");


module.exports = merge(common, {
  mode: 'production',  
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, "css-loader"],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
        filename: "[name].css",
        chunkFilename: "[id].css",
      }),

    new HtmlWebpackPlugin({
      meta: {
            'viewport': 'width=device-width, initial-scale=1, shrink-to-fit=no',
      },
      title: 'Production',
    }),
  ],
  optimization: {
    minimizer: [
      new CssMinimizerPlugin(),
    ],
  },
});