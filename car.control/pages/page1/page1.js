// pages/page1/page1.js
Page({
  onReady:function(e){
    this.audioCtx= wx.createAudioContext('myAudio')
  },
  /**
   * 页面的初始数据
   */
  data: {
    action: {
      method: ''
    },
    poster:'http://imgcache.qq.com/music/photo/album_300/17/300_albumpic_13563902_0.jpg',
    name:'忘川彼岸',
    author:'零一九零贰',
    src:'http://ws.stream.qqmusic.qq.com/C4000036xFot0ifWDn.m4a?guid=6832576894&vkey=5B9861E517FB50958594119B51BDBE08C02D9594522E60AD63A7C041C05572E626E04EC479E374BFFED0DC8239667DB21D9496DBF4F22325&uin=0&fromtag=66'
  },
  audioPlay:function()
  {
   //this.audioCtx1.play()
    this.setData({
      action: {
        method: 'play'
       
      }
    })
  },
  audioPause:function()
  {
    this.setData({
      action: {
        method: 'pause'
      }
    })
  },
 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})