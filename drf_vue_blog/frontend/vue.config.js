const webpack = require('webpack')


module.exports = {
  lintOnSave: false,
  devServer: {
      proxy: {
          '/api': {
              target: `http://127.0.0.1:8000/api`,
              changeOrigin: true,
              pathRewrite: {
                  '^/api': ''
              }
          }
      }
  },

  configureWebpack:{
      plugins:[
          new webpack.ProvidePlugin({
              $:"jquery",
              jQuery:"jquery",
              "windows.jQuery":"jquery"
          })
      ]
  },
};