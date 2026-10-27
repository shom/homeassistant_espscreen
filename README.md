<p align="center">
  <a href="https://tessera-maxgramser.on-forge.com"><img src="docs/images/tessera-mosaic.jpg" width="100%" alt="A mosaic of real Tessera screens in every size, from the 2.8-inch CYD to the 10.1-inch Guition: lights, music, the thermostat, the weather, locks, blinds and the vacuum, in light and dark mode"></a>
</p>

<p align="center">
  <a href="https://tessera-maxgramser.on-forge.com"><img src="docs/images/tessera-mark.svg" width="112" alt="The Tessera logo: four rounded tiles in yellow, blue, purple and green, like a small mosaic"></a>
</p>

<h1 align="center">Tessera</h1>

<p align="center"><b>Home Assistant 触摸屏：每个房间一块屏，一个简单的编辑器。</b></p>

<p align="center">
  <a href="https://tessera-maxgramser.on-forge.com">官网</a> ·
  <a href="https://tessera-maxgramser.on-forge.com/docs/quick-start">快速开始</a> ·
  <a href="https://tessera-maxgramser.on-forge.com/screens">支持的屏幕</a> ·
  <a href="https://tessera-maxgramser.on-forge.com/community">社区</a> ·
  <a href="https://tessera-maxgramser.on-forge.com/community/share?type=installation">我的屏幕实装</a>
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fshom%2Fhomeassistant_espscreen"><img src="https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg" alt="Add the Tessera repository to your Home Assistant"></a>
</p>

<p align="center"><sub>Tessera 不在默认应用商店里。这个按钮会把它的仓库添加到你的 Home Assistant。之后 Tessera Screen Manager 就和其他应用一样出现在商店中。</sub></p>

<p align="center"><sub>Tessera 是 ESP Screens 的新名字。在 Home Assistant 中应用名为 Tessera Screen Manager，面板名为 Tessera；仓库、插件和你的屏幕都保持原样。</sub></p>

<p align="center"><sub>找电子墨水屏？Tessera 面向彩色 LCD 触摸屏。若想在 e-ink 面板上做安静的信息面板，看看 <a href="https://tesserae.ink">Tesserae（tesserae.ink）</a>——一个名字相似、面向 Home Assistant 的独立开源项目。</sub></p>

谢谢你！我怀着热爱维护这个项目，每一份支持都有帮助。我真心热爱 Home Assistant 社区。

我负责 Tessera 的开发与维护，社区也有贡献。你的支持能让我有更多时间开发、审查和测试改进。欢迎按月小额赞助或请一杯咖啡。

<p align="center">
  <a href="https://discord.gg/M7x96AUzC"><img src="docs/images/discord-invite.svg" width="560" alt="Join our brand-new Discord and help build the Tessera community."></a>
</p>

<p align="center"><a href="https://discord.gg/M7x96AUzC"><b>加入我们全新的 Discord</b></a></p>

<a href="https://buymeacoffee.com/f5j9jnkmhpv/membership"><img src="https://img.buymeacoffee.com/button-api/?text=Support%20monthly&emoji=&slug=f5j9jnkmhpv&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" alt="Support monthly" height="42"></a>
&nbsp; 或 <a href="https://buymeacoffee.com/f5j9jnkmhpv">请我喝一杯咖啡</a>

<p align="center">
  <img src="docs/images/photo-guition-page-2.jpg" width="49%" alt="The Guition 4-inch screen on a table: the Evening page with Movie night and Good night in pastel lilac and blue, and the ceiling light and the bedroom fan as tall tiles with their sliders">
  <img src="docs/images/photo-guition-vacuum.jpg" width="49%" alt="The vacuum card on the Guition: docked at 100 %, Start cleaning and Dock, and the suction from Quiet to Max">
</p>

**一块由你自己排布、由 Home Assistant 管理的触摸屏。**安装和使用都极其简单。

**为什么做这个。**手机在另一个房间，墙挂平板又太贵。一块小型 ESP32 触摸屏只要零头价钱，放在桌上或装进墙盒，随时触手可及地控制灯光、地暖或扫地机器人。

**这是什么。**面向平价面板的固件，目前支持五块：从 2.8 英寸 CYD 到 10.1 英寸 Guition。卡片最多八页，内存大的板子还可以更多，每页放多少取决于玻璃：灯光、温控、实时能源曲线、时钟与计时器、带键盘的安防面板、摄像头、家人位置地图，一张卡片可以占满整页——不看屏幕也能按的大开关，也可以是一张跳转到其他页面的导航卡。门铃响时，自动化可以把警报推到每一块屏幕上；有图片内存的屏幕还能显示门铃摄像头拍到的来人。点按可以运行 Home Assistant 为卡片提供的任何动作；深色模式适合放在床头的屏幕。

**怎么做。** Tessera Screen Manager 是 Home Assistant 里的一个应用。它通过 USB 为新屏幕烧录固件，通过 Wi-Fi 更新，并把卡片发到屏幕上。改屏幕就是挑选、拖放、**保存并发送**：不重刷固件，不写 YAML，不用 blueprint、MQTT 或令牌。亮度、夜间时段和深色模式也能在屏幕上或用自动化更改，而且你为某块屏幕写的自定义 YAML 在每次更新后都保留。

**[安装](#从-home-assistant-安装)** · [官网手册](https://tessera-maxgramser.on-forge.com/docs/) · [页面](https://tessera-maxgramser.on-forge.com/docs/pages) · [屏幕设置](https://tessera-maxgramser.on-forge.com/docs/screen-settings) · [疑难解答](https://tessera-maxgramser.on-forge.com/docs/troubleshooting) · [更新日志](screen_manager/CHANGELOG.md)

> **手册在 [Tessera 网站](https://tessera-maxgramser.on-forge.com/docs/)上：**从[快速开始](https://tessera-maxgramser.on-forge.com/docs/quick-start)到每张卡片、每块屏幕设置、每块支持的屏幕与疑难解答，都带搜索。任何 GitHub 账号都可以通过每页的“Edit this page”改进手册。本 README 只是总览；docs/ 下的文件是面向贡献者的参考。

## Requests, questions and bugs

> **GitHub Issues 只收 bug。**提交在 GitHub 上的功能请求和新板板请求不会被处理。请到 [Tessera 愿望清单](https://tessera-maxgramser.on-forge.com/wishlist)提交和讨论。

- **功能与改进：**在[愿望清单](https://tessera-maxgramser.on-forge.com/wishlist)里搜索。给已有的愿望投票，或新增一个。
- **新的 ESP 板卡与显示屏：**在愿望清单的[新板分类](https://tessera-maxgramser.on-forge.com/wishlist?category=board)提交，附上确切型号、商品链接以及你是否能参与测试。票数体现多少人需要，帮助排定优先级，但不保证支持或发布日期。
- **提问与示例：**发到[社区](https://tessera-maxgramser.on-forge.com/community)，原先 GitHub 上的讨论和回复都搬到了那里。
- **Bug：**属于现有功能损坏的问题用 GitHub Issues。请附上可复现步骤和版本信息。
- **代码改动：**开 pull request，并在描述中关联其修复的 bug 或实现的网站愿望。

在网站上用 GitHub 登录即可投票、发帖或回复。发帖前先搜索，让讨论和投票聚在一起。

## 真实场景

客厅里的 Guition，37 秒一镜到底：点卡片、翻页面、打开详情卡和历史曲线，身后的灯从紫色变到橙色。

https://github.com/user-attachments/assets/f9f6a933-d388-4c8b-9c9a-011dfa37617b

<p align="center">
  <img src="docs/images/photo-guition-home.jpg" width="32%" alt="The Guition on a wooden sideboard beside a glowing purple lamp: the living room page with the airco, an analog clock with the date, two scenes and a dimmer at 36 percent">
  <img src="docs/images/photo-guition-history.jpg" width="32%" alt="The same screen showing a temperature history over 24 hours, with its highest and lowest point marked and the 1 hour, 24 hours and 1 week keys">
  <img src="docs/images/photo-guition-light.jpg" width="32%" alt="The light card of the purple lamp: the colour slider at 304 degrees, the brightness slider at 20 percent and the effects key at the top right">
</p>
<p align="center"><sub>真实照片，不是渲染图：4 英寸 Guition 和它控制的灯。</sub></p>

## 打印一个屏幕支架

屏幕配上专门为其设计的支架最好看。这些支架可在 MakerWorld 免费下载打印，每个都带现成的 Bambu Studio 打印配置，无需支撑。

<p align="center">
  <a href="https://makerworld.com/en/models/3485702"><img src="docs/images/stand-d1001.jpg" width="32%" alt="A Seeed reTerminal D1001 on a round white printed base on a wooden desk, showing a Tessera page with the clock, the weather, music, a camera and the lights"></a>
  <a href="https://makerworld.com/en/models/3410079"><img src="docs/images/stand-guition-v2.jpg" width="32%" alt="The 4-inch Guition in a black printed wedge stand on a wooden table, showing a home page with the weather, a speaker, the airco and two lights"></a>
  <a href="https://makerworld.com/en/models/3389654"><img src="docs/images/stand-guition.jpg" width="32%" alt="The 4-inch Guition in an upright black printed stand on a wooden table, beside a window"></a>
</p>

- **[Home Assistant 平板底座](https://makerworld.com/en/models/3485702)**，适配 Seeed reTerminal D1001（8 英寸）：圆形底座带停泊槽，倾斜 30 度。两条打印导轨通过 VESA 孔固定屏幕，用四颗 M4×8 mm 螺丝。内置的 ESP32-P4 可实时播放摄像头并与 Assist 对话。
- **[楔形支架](https://makerworld.com/en/models/3410079)**，适配 Guition 4 英寸 ESP32-S3-4848S040：简洁的楔形支架，让方形屏幕处于舒适角度。先取下屏幕背面的小背板（背面两颗小螺丝），再推入即可。
- **[直立支架](https://makerworld.com/en/models/3389654)**，同样适配 Guition 4 英寸：Tessera 的第一款支架，扬声器格栅上有个小心心。把屏幕推入即可，无需螺丝。

**已经打印了？**在 MakerWorld 上点个赞或 Boost 不花一分钱，能帮助 Tessera 保持免费；带着你自己布局的成品照片也永远欢迎。

## 支持五块屏，2.8 到 10.1 英寸

一个家，五块面板。每块屏幕都为它运行的玻璃量身构建：开机时测量自己的画布，把该板拥有的格数分配给页面——2.8 英寸 CYD 每页 6 张卡片，10.1 英寸 Guition 每页 25 张——而卡片本身的大小以毫米计基本不变。同样的卡片、同样的详情、同一个编辑器；玻璃越大，一页装得下的家就越多。每块板以适合其玻璃的网格起步，编辑器可以在页面旁直接改行列数，无需重新构建：10.1 英寸 Guition 在八行布局下单页最多四十张卡片。

<p align="center">
  <img src="docs/images/boards-scale.png" width="98%" alt="The five supported screens side by side on one scale, each showing a page of the same home: the small 2.8-inch CYD, the square 4-inch Guition, the wide 4.3-inch Waveshare, the 7-inch Waveshare and the large 10.1-inch Guition">
</p>
<p align="center"><sub>等比绘制，每块屏配它铺满的页面：同一个家在 2.8 英寸 CYD、4 英寸 Guition、4.3 与 7 英寸 Waveshare 和 10.1 英寸 Guition 上。由固件自己的代码逐板渲染。</sub></p>
<p align="center">
  <img src="docs/images/board-cyd.png" width="32%" alt="The kitchen page on the 2.8-inch CYD: the weather with five days, a pasta timer, the coffee machine, the kitchen lamp and the power usage">
  <img src="docs/images/board-guition.png" width="32%" alt="The Good morning page on the 4-inch Guition: an analog clock with the time and the date, the weather for four days, the coffee machine in orange and Sam at home">
  <img src="docs/images/board-waveshare43.png" width="32%" alt="The front door page on the 4.3-inch Waveshare: the front door camera live on a tile of two by two cells, the lock, the porch light, the weather and Sam">
</p>
<p align="center">
  <img src="docs/images/board-waveshare7.png" width="49%" alt="The living room page on the 7-inch Waveshare: the album cover on a tile of two by two cells, a clock with the date, the weather for five days, the heating and the curtains one cell wide and two high, a temperature graph and a lamp dimmer">
  <img src="docs/images/board-jc8012p4a1.png" width="49%" alt="The living room page on the 10.1-inch Guition: twenty-five cells with a clock, the weather, Sam, the album cover and the front door camera on two by two tiles each, the heating two cells high, graphs for the temperature and the energy, a lamp dimmer, the coffee machine, the robot and a good-night script">
</p>
<p align="center">
  <img src="docs/images/boards-standing.png" width="66%" alt="Two of the same screens built standing up, to scale: the 10.1-inch Guition with the same living room page in five columns of tall cells, and the 7-inch Waveshare by the front door with a clock, the weather, the front door camera, the lock, the porch light, the heating, Sam and the alarm in two columns">
</p>
<p align="center"><sub>同一个家的竖屏形态。除正方形外的每块板都可横可竖，安装屏幕时选择，之后在编辑器里随时更改且无需重刷，竖屏有自己独立的网格：7 英寸 Waveshare 由 4×4 变为 2×7，10.1 英寸 Guition 在高格下保持 5×5。哪块板是哪块、购买时看什么：<a href="#哪块屏幕">选屏指南</a>。</sub></p>
<p align="center">
  <img src="docs/images/jc8012p4a1-6rows.png" width="49%" alt="The living room on the 10.1-inch Guition with six rows, thirty cells: a clock, the weather for five days with the chance of rain, Sam, the album cover and the front door camera live on two by two tiles, the heating two cells high, graphs for the temperature and the energy, a lamp dimmer, the lock, the ceiling light, the robot, the curtains and two scenes">
  <img src="docs/images/jc8012p4a1-7rows.png" width="49%" alt="The same living room with seven rows, thirty-five cells: the alarm, the porch light, a second thermostat for the hallway and the coffee machine join the page">
</p>
<p align="center">
  <img src="docs/images/jc8012p4a1-8rows.png" width="49%" alt="The same living room with eight rows, forty cells: a kitchen speaker with its cover and volume, a small live porch camera, the kitchen lights and Alex fill the last row">
  <img src="docs/images/jc8012p4a1-8rows-dark.png" width="49%" alt="The page with eight rows in Dark mode">
</p>
<p align="center"><sub>10.1 英寸 Guition 的六、七、八行布局，每页从三十到四十张卡片，以及深色模式下的八行。由固件自己的代码渲染。编辑器在页面旁改行数，布局自动跟随：一页放不下的卡片会移到其后新建的页面。感谢 <a href="https://github.com/Heronimonimo">Jeroen Peters</a> 的<a href="https://github.com/MaxGramser/homeassistant_espscreen/pull/151">多行支持</a>。</sub></p>

## 全屋能源，实时显示

<p align="center">
  <img src="docs/images/energy-jc8012p4a1-dark.png" width="98%" alt="The 10.1-inch Guition in Dark mode with the energy card on three by three cells: the sun gives 5.2 kW, the house uses 2.5 kW, the battery at 64 % charges with 1.5 kW and 1.2 kW goes back to the grid, with lines and moving dots between their circles and the heat pump, the fridge, the washing machine and the office around the house; beside it the weather, the solar energy of today, the EV charger, the battery and graphs of the solar power and the living room temperature">
</p>
<p align="center">
  <img src="docs/images/energy-guition.png" width="32%" alt="The energy card on two by two cells of the 4-inch Guition: solar, grid, battery and the house with their power, above the solar energy of today and the EV charger">
  <img src="docs/images/energy-waveshare43.png" width="41%" alt="The 4.3-inch Waveshare with the energy card two cells wide and three high, beside the solar energy of today, the EV charger and the battery">
  <img src="docs/images/energy-cyd-standing.png" width="20%" alt="The 2.8-inch CYD standing up with the energy card over its whole page, the diagram turned upright: the grid at the top, solar and the battery at the sides and the house at the bottom">
</p>
<p align="center">
  <img src="docs/images/energy-guition-history.png" width="32%" alt="A tap on the solar circle opens the history of the solar sensor: a day with its highest and lowest moment">
  <img src="docs/images/energy-waveshare7-dark.png" width="49%" alt="The 7-inch Waveshare in Dark mode with the energy card on three by three cells and four devices, and the weather, the solar energy of today, the EV charger, the battery, the kitchen light, the heat pump and the car's battery beside and under it">
</p>
<p align="center"><sub>能源卡片实时显示全屋电力，呈现方式与 Home Assistant 自带的实时能源视图和 power-flow-card-plus 相同：太阳能、电网和电池环绕全家，功率越大圆点流得越快，并列出耗电最多的设备。它直接读取你在 Home Assistant 里已有的能源设置，无需任何配置；点按某个圆圈即可打开该传感器的历史。适配每一块屏，竖屏同样支持（<a href="docs/ENERGY.md">原理</a>）。由固件自己的 LVGL 代码用一个虚构的家庭渲染。</sub></p>

## 每个传感器都能上仪表

<p align="center">
  <img src="docs/images/meters-jc8012p4a1-bars-dark.png" width="98%" alt="The 10.1-inch Guition in Dark mode with a page of sensors as LCD bars: the living room at 21.4 degrees on a big amber bar, the office CO2 at 840 ppm, the bathroom humidity and the phone's battery standing up, the house's power in purple, the CPU, the disk and the memory, the wind, the outside temperature in light blue and the bedroom CO2 at 1,260 ppm, whose cells turn from green to orange to red where its thresholds are">
</p>
<p align="center">
  <img src="docs/images/meters-jc8012p4a1-rings.png" width="49%" alt="The 10.1-inch Guition with a page of rings: the living room and the solar power two by two, each with its ring on the left and the last 24 hours as a line on the right, the office CO2, the bathroom and the phone's battery as big rings, and smaller rings for the CPU, the disk, the memory, the outside temperature, the wind, the pressure, the grid, the fridge and the freezer">
  <img src="docs/images/meters-jc8012p4a1-tapes-dark.png" width="49%" alt="The same screen in Dark mode with a page of tapes in the style of Teenage Engineering: the name in small capitals, the value large, a still ruler of fine marks over the sensor's range with one pointer at the value, for the rooms, the outside, the humidity, the pressure, the solar power, the wind, the fridge, the noise, the daylight and the office CO2">
</p>
<p align="center">
  <img src="docs/images/meters-guition.png" width="24.5%" alt="The 4-inch Guition: the phone's battery as a ring, the humidity as a tape, the house's power as a bar of cells, and the living room as a ring with its day beside it">
  <img src="docs/images/meters-waveshare43-dark.png" width="40.8%" alt="The 4.3-inch Waveshare in Dark mode: the living room as a ring with its day, the phone's battery, the office CO2 as a big value over a bar of cells, the house's power as a tape, the CPU as a ring and the humidity as a tape">
  <img src="docs/images/meters-cyd.png" width="32.7%" alt="The 2.8-inch CYD: the office CO2 as a bar, the living room as a tape, the outside temperature as a ring and the pressure as a tape over its range from 980 to 1040 hPa">
</p>
<p align="center"><sub>任何状态为数值的传感器都能展示当前读数：带图标的圆环、带指针刻度条的条带，或铺满卡片的 LCD 格子条。每种外观都能填满它拿到的空间，从一个格子到整页，并随尺寸放大。量程来自 Home Assistant（百分比即 0 到 100），也可由卡片自定义；颜色可用传感器自己的、手选的，或两三段绿/橙/红分段，在传感器单位的阈值（如 800 和 1200 ppm）处切换。在显示方式里选“仪表”。下个版本的新功能；dev 渠道已可用。由固件自己的 LVGL 代码用虚构传感器渲染。</sub></p>

## 更高的卡片，更丰富的控制

<p align="center">
  <img src="docs/images/tall-jc8012p4a1.png" width="98%" alt="The 10.1-inch Guition in Dark mode: a clock with the date, the weather for five days, a media tile two cells wide and two high with the album cover dimmed behind the title and the play keys, the front door camera live beside it, the heating one cell wide and two high with minus, plus and its mode keys, graphs for the temperature and the energy, a table lamp dimmer, the coffee machine, the robot and a good-night script">
</p>
<p align="center">
  <img src="docs/images/tall-guition-media.png" width="32%" alt="The 4-inch Guition: a media tile two by two with the album cover behind the track, the artist and the previous, pause and next keys, above a table lamp with its dimmer">
  <img src="docs/images/tall-guition-climate.png" width="32%" alt="The Comfort page: the heating one cell wide and two high with its setpoint between minus and plus and its mode keys, heat lit in orange, the curtains open at 70 % with a slider, and a temperature graph">
  <img src="docs/images/tall-guition-home.png" width="32%" alt="The Evening page: Movie night and Good night in pastel lilac and blue, and two tiles one cell wide and two high: the ceiling light at 59 % and the bedroom fan, each with a big slider">
</p>
<p align="center">
  <img src="docs/images/tall-waveshare43-media.png" width="49%" alt="The 4.3-inch Waveshare: the media tile two by two with its album cover, the heating one cell wide and two high, a lamp dimmer and Sam at home">
  <img src="docs/images/tall-waveshare43-climate.png" width="49%" alt="The same screen in Dark mode: the bedroom thermostat two by two with its setpoint between minus and plus, the curtains one cell wide and two high, a temperature graph and the coffee machine">
</p>
<p align="center"><sub>卡片除了单格、双倍宽和整页，还可以是 1×2 或 2×2 格，内容随空间变化：播放器把专辑封面垫在曲目后面（CYD 除外），地暖显示设定温度和 Home Assistant 列出的模式（放不下时最后一个键打开卡片），窗帘显示位置、空间够时还有百叶角度，而两格高的灯、开关、脚本或场景就是一颗大按键。每块板从自己的玻璃计算出同样的卡片。每页有自己的标题和顶栏，任何页面可设为主页，页面也可以不进页码圆点、改由卡片打开，并带返回键。由固件自己的 LVGL 代码用一个演示之家渲染。</sub></p>

## 天气、地暖、摄像头、安防与门锁

<p align="center">
  <img src="docs/images/guition-weather-tiles.png" width="32%" alt="The 4-inch Guition with two weather tiles: a wide one with today and the next three days, and a big one listing the days under each other, each with a coloured bar from its low to its high on one scale">
  <img src="docs/images/guition-thermostat-tiles.png" width="32%" alt="Three thermostats: the heating with its setpoint between minus and plus and a bar with Heat and Auto, an airco on cool with heat, cool and more behind three dots, and a wide bedroom tile with the stepper on one row">
  <img src="docs/images/guition-camera-fill.png" width="32%" alt="A garden camera on a tile of two by two cells, its picture filling the whole card with the camera's name at the bottom, above the garden lights and the garden temperature">
</p>
<p align="center">
  <img src="docs/images/guition-alarm-tiles.png" width="32%" alt="Four alarm panels as tiles: the house disarmed in grey, the garage armed away in green, the shed arming in orange and the studio armed home in green">
  <img src="docs/images/guition-alarm-card.png" width="32%" alt="The alarm card: the shield in its circle, keys for Home, Away, Night and Vacation, and the Disarmed key">
  <img src="docs/images/guition-alarm-keypad.png" width="32%" alt="The keypad to arm away: four dots for the code, the digits 1 to 0, a clear key and a check key">
</p>
<p align="center">
  <img src="docs/images/guition-lock-tiles.png" width="32%" alt="Six locks as tiles: the front door asking to confirm in orange, the back door unlocked in red, the gate locked in green, the garage jammed in red, the shed locking in orange and the cellar unavailable in grey">
  <img src="docs/images/guition-lock-card.png" width="32%" alt="The lock card: a big green lock to tap with Unlock under it, and an Open door key">
  <img src="docs/images/guition-lock-confirm.png" width="32%" alt="The lock card waiting for the second tap: the big lock orange and open, with Confirm under it">
</p>
<p align="center">
  <img src="docs/images/waveshare43-new-tiles.png" width="49%" alt="The 4.3-inch Waveshare: a wide weather tile with the coming days, the bedroom thermostat, a garden camera filling a tile of two by two cells, the washing machine on Cotton eco and the dryer">
  <img src="docs/images/waveshare43-select-card.png" width="49%" alt="The select card of a washing machine on the 4.3-inch Waveshare: its programmes in two columns, Cotton eco checked, and page dots for the rest">
</p>
<p align="center"><sub>天气显示未来几天，更大的卡片显示整周并带每天低温到高温的色条。温控器有 − / + 和每个模式一个按键的模式条；空调先显示制热制冷，其余收进“…”。实时摄像头在更高的卡片上铺满整卡并显示名称，或完整显示画面。安防面板按 Home Assistant 的配色显示为卡片，每个模式一个按键，需要密码时给出 Home Assistant 的键盘；有人闯入会唤醒所有屏幕并弹键盘撤防。门锁一次点按上锁，解锁前要求再点一次；卡片在锁支持开锁舌时有开门键，锁要求密码时给出 Home Assistant 的键盘。选择器（如洗衣机的程序）打开一个列表并勾选当前项。在内存足够的屏幕上，每一页都提前构建并保留，翻过去的那一刻内容已经就绪。由固件自己的 LVGL 代码用一个演示之家渲染。</sub></p>

## 音乐，从音箱到媒体库

<p align="center">
  <img src="docs/images/media-boards-scale.png" width="98%" alt="The same player card on five screens side by side on one scale, from the 2.8-inch CYD to the 10.1-inch Guition: the album cover on a ground in its own colours, the speaker Kitchen at the top, the title, the bar through the track, the keys and the volume">
</p>
<p align="center">
  <img src="docs/images/media-guition-player.png" width="32%" alt="The player card on the 4-inch Guition: the album cover on a ground in the cover's own colours, the speaker Kitchen at the top, the title and artist, a bar to drag through the track, shuffle, previous, pause, next and repeat, and the volume">
  <img src="docs/images/media-guition-speakers.png" width="32%" alt="The speaker menu open over the card: Bedroom, Kitchen with a check mark, and Living room">
  <img src="docs/images/media-guition-favourites.png" width="32%" alt="A page of favourites: an album and a playlist with their covers dimmed behind the name and a play key, the playlist that plays ringed in blue with a pause key, an artist and the player itself">
</p>
<p align="center">
  <img src="docs/images/media-guition-library.png" width="32%" alt="The library of the player: Playlists, Artists, Albums, Liked songs, Podcasts, Recently played, Top artists and Top tracks">
  <img src="docs/images/media-guition-albums.png" width="32%" alt="A page of albums: six covers with their titles, page dots and arrows to turn to the next six">
  <img src="docs/images/media-cyd-favourites.png" width="32%" alt="The same favourites on the 2.8-inch CYD, drawn with icons: an album, two playlists, an artist and the player">
</p>
<p align="center">
  <img src="docs/images/media-waveshare43-player.png" width="49%" alt="The player card on the 4.3-inch Waveshare: the cover at the left on its coloured ground, the title, the bar and the keys beside it, the volume along the bottom">
  <img src="docs/images/media-waveshare43-albums.png" width="49%" alt="A page of albums on the 4.3-inch Waveshare: five covers in a row with page arrows">
</p>
<p align="center">
  <img src="docs/images/media-waveshare43-starting.png" width="49%" alt="Favourites on the 4.3-inch Waveshare: the wide favourite Sunday Morning starting on the Kitchen speaker, a spinner round its play key">
  <img src="docs/images/media-waveshare43-speakers.png" width="49%" alt="The speaker menu over the player card on the 4.3-inch Waveshare: Bedroom, Kitchen with a check mark, and Living room">
</p>
<p align="center">
  <img src="docs/images/media-jc8012p4a1-albums.png" width="66%" alt="A page of albums on the 10.1-inch Guition: eighteen covers in three rows of six">
</p>
<p align="center"><sub>媒体播放器卡片以正在播放的封面颜色为底，播放的音箱在顶部：点按即可把音乐切到另一个音箱。随机、循环和拖动进度的进度条在标题下方。媒体库键打开 Home Assistant 在该播放器上可浏览的内容，一层层进入封面页，点封面即播放。收藏是一张卡片，在指定的音箱上播放一个播放列表、专辑或歌手，封面垫底；闲置的播放器保留卡片，方便选好音箱直接开播。这里没有任何专为某个服务写死的东西：一切就是 Home Assistant 上报的播放器与其媒体库，所以 Spotify 和其他可浏览的播放器没有区别。封面与媒体库需要一块有图片内存的屏幕（<a href="https://tessera-maxgramser.on-forge.com/docs/cameras">原理</a>）；CYD 保留卡片、音箱选择和收藏，以图标绘制。由固件自己的 LVGL 代码用虚构的媒体记录渲染。</sub></p>

## 每个人在哪里

<p align="center">
  <img src="docs/images/guition-map.png" width="25%" alt="The 4-inch Guition with a map tile of two by two cells: the streets and canals of a city in soft greys, a marker for each person with a photo or initials and their first name beside it, and the tile's name Family at the bottom, above a lamp and a temperature">
  <img src="docs/images/guition-map-dark.png" width="25%" alt="The same map tapped open over the whole screen in Dark mode: dark streets, the people in their own colours, the round back key and the name Family at the top">
  <img src="docs/images/waveshare43-map.png" width="41%" alt="The 4.3-inch Waveshare with the map tile following everyone: four people, two with a photo in their marker, and a car">
</p>
<p align="center"><sub>人员卡片可以是一张地图，显示此人及与其同行的人的位置；地图卡片可跟随 Home Assistant 知道位置的所有人，也可只跟随你选的人。标记里是照片，配色与 Home Assistant 自带地图一致；点按全屏打开地图。Tessera 用屏幕自己的配色（浅色或深色）基于 Home Assistant 的地图瓦片绘制，只在有人移动时重绘；屏幕收到的只是图片，永远不会拿到位置（<a href="docs/MAP.md">原理</a>）。由固件自己的 LVGL 代码用一个虚构的家庭渲染；地图数据 © OpenStreetMap 贡献者。</sub></p>

## 床头的时钟

<p align="center">
  <img src="docs/images/guition-bedside.png" width="49%" alt="The bedside clock on the 4-inch Guition in dark mode: 23:47 in large grey digits on a black page, and under it three round keys: the bedside lamp on in amber, the front door locked in green and the alarm armed for the night in green">
</p>
<p align="center"><sub>床头时钟占据整页：时间尽可能大，下方最多三颗圆形按键放你夜里伸手要用的东西。按键就是圆形形态的卡片，行为与它的卡片一致：灯一点即开，前门锁解锁前要求再点一次，安防面板显示当前布防状态。配合深色模式和屏幕的夜间时段，页面全黑、背光变暗。由固件自己的 LVGL 代码用一个演示之家渲染。</sub></p>

## 屏幕上都有什么

<p align="center">
  <img src="docs/images/guition-front-door.png" width="32%" alt="The Front door page on the Guition 4-inch screen: the front door camera live on a tile of two by two cells with its name, the front door locked and the porch light on">
  <img src="docs/images/guition-energy.png" width="32%" alt="The Energy page: today's energy as a graph, the power and the humidity as large values, and the robot vacuum with start, stop and dock">
  <img src="docs/images/guition-weather-page.png" width="32%" alt="The Weather page: the garden forecast on a big tile, each day with a bar from its low to its high, above the sun's path with sunrise and sunset">
</p>
<p align="center">
  <img src="docs/images/guition-full-light.png" width="32%" alt="A full-page tile: one big amber light switch that fills the screen, so you push anywhere without looking">
  <img src="docs/images/guition-full-menu.png" width="32%" alt="Navigation tiles: Heating, Blinds and Weather each open their own page, next to a person and a lamp">
  <img src="docs/images/guition-full-climate.png" width="32%" alt="A full-page heating tile: the room temperature big in the middle, the mode keys at the bottom">
</p>
<p align="center">
  <img src="docs/images/guition-weather.png" width="32%" alt="Weather card: current weather, the coming hours and the coming days with chance of rain">
  <img src="docs/images/guition-climate.png" width="32%" alt="Climate card: the target temperature between big minus and plus keys, the mode keys, and fan and swing choices">
  <img src="docs/images/guition-light.png" width="32%" alt="Light control: color, color temperature and brightness">
</p>
<p align="center">
  <img src="docs/images/guition-vacuum.png" width="32%" alt="Vacuum card: docked at 100 %, Start cleaning and Dock, and the suction from Quiet to Max">
  <img src="docs/images/guition-blind.png" width="32%" alt="Cover card for a venetian blind: its battery, the position slider with the blind hanging from the top, the tilt slider over slats, and open, stop and close">
  <img src="docs/images/guition-history-touch.png" width="32%" alt="A finger on the history graph: the top of the card shows the average of that hour and its time, the graph stays as it is">
</p>
<p align="center">
  <img src="docs/images/guition-effects.png" width="32%" alt="The effects page of a WLED lamp: the effect, colour palette, preset and playlist rows with what they are set to, and the speed and intensity sliders">
  <img src="docs/images/guition-effects-picker.png" width="32%" alt="The effect picker: a drum with every effect Home Assistant lists, TV Simulator in the middle, and the check key at the top right that sends it">
  <img src="docs/images/cyd-effects.png" width="32%" alt="The same effects page on the CYD: four rows and the two sliders in 320 by 240 pixels">
</p>
<p align="center"><sub>点按卡片即开关，长按打开完整卡片。按键和滑条直接放在卡片上，淡彩配色，时钟、天气和历史都适合手指阅读。带模式的灯（如 WLED）会有一个效果页，带转盘选择器，名称和内容来自 Home Assistant 列出的效果。由固件自己的 LVGL 代码用一个演示之家渲染。</sub></p>
<p align="center">
  <img src="docs/images/guition-camera-tiles.png" width="32%" alt="Cameras as tiles on the Guition: the front door camera filling a tall tile with its name at the bottom, a porch camera showing its whole picture with black above and below, the porch light and Sam at home">
  <img src="docs/images/guition-camera.png" width="32%" alt="A camera tile tapped: the front door camera full screen, with the round back key and the camera's name at the top">
  <img src="docs/images/guition-alert-camera.png" width="32%" alt="The same camera in an alert: its picture across the top of the card, with the card's rounded corners">
</p>
<p align="center"><sub>摄像头不只是警报的一部分，它本身就是卡片：Home Assistant 里任何摄像头或快照（比如门铃最后一次响铃）都能像其他卡片一样放到屏幕上。点按全屏看画面，每四秒刷新；或让卡片自己显示实时画面（显示方式 → 实时画面，每 5 到 30 秒），铺满或完整显示，带不带名称都行，最大可到整页；警报也可以携带同样的画面。除 CYD、Waveshare 3.5 英寸和 Hosyond 4 英寸（无图片内存，<a href="https://tessera-maxgramser.on-forge.com/docs/cameras">原理</a>）外的所有屏幕均支持。</sub></p>
<p align="center">
  <img src="docs/images/cyd-home.png" width="32%" alt="CYD 2.8-inch screen: the weather forecast, a pasta timer, the coffee machine in orange, the kitchen lamp and the power usage as a large value">
  <img src="docs/images/cyd-page-2.png" width="32%" alt="Second CYD page: the Sonos volume, Sam at home, the Movie night scene in lilac and an energy graph">
  <img src="docs/images/cyd-weather.png" width="32%" alt="The weather card on the CYD: current weather, the coming hours and the coming days">
</p>
<p align="center">
  <img src="docs/images/cyd-tiles-controls.png" width="32%" alt="The CYD with heating mode keys, playback keys for the radio and a ceiling fan's speed slider">
  <img src="docs/images/cyd-vacuum.png" width="32%" alt="The vacuum card on the CYD: docked at 100 %, clean and dock, and the suction from Quiet to Max">
  <img src="docs/images/cyd-history.png" width="32%" alt="The history card on the CYD: power over 24 hours with its highest and lowest moment, an axis in watts and clock times">
</p>
<p align="center">
  <img src="docs/images/cyd-media.png" width="32%" alt="The media card on the CYD on the colours of its cover: the player's icon where the cover would be, the title, artist and album, the bar with its times, the keys and the volume slider">
  <img src="docs/images/cyd-media-full.png" width="32%" alt="A media player over the whole CYD page: the icon at the left, the track and the keys beside it, the volume row along the bottom">
  <img src="docs/images/cyd-dark-media.png" width="32%" alt="The media card on the CYD in dark mode">
</p>
<p align="center"><sub>同样的卡片在 2.8 英寸 CYD（320 × 240）上。CYD 没有图片内存：媒体卡片在封面的位置显示播放器图标。</sub></p>
<p align="center">
  <img src="docs/images/guition-dark-home.png" width="32%" alt="Dark mode on the Guition: the living room page on a black page, the album cover and the lamp dimmer in their own colours">
  <img src="docs/images/guition-dark-controls.png" width="32%" alt="Dark mode on the Good morning page: graphite cards and soft white text, the clock, the weather, the coffee machine in a deep orange and Sam">
  <img src="docs/images/guition-dark-page-4.png" width="32%" alt="Dark mode on the Evening page: the two scenes in deeper lilac and blue, and the tall ceiling light and fan sliders keep their colours">
</p>
<p align="center"><sub>深色模式，为床头屏幕准备：同样的页面，更深的配色。它是屏幕上的一个开关，也在 Tessera 和 Home Assistant 里，自动化可以在睡觉时间自动打开。</sub></p>
<p align="center">
  <img src="docs/images/guition-settings-screen.png" width="32%" alt="The settings page on the Guition, Screen: back to Home by itself and after how long, also on standby, swiping between pages and the page buttons, with the rotation on its second page">
  <img src="docs/images/guition-settings.png" width="32%" alt="The settings page on the Guition, Brightness: the brightness with minus and plus, Dark mode off, Auto standby on, standby after 10 minutes and the standby brightness">
  <img src="docs/images/guition-dark-settings.png" width="32%" alt="The same Brightness page right after turning Dark mode on: a black page with graphite rows and soft white text">
</p>
<p align="center"><sub>屏幕上直接设置：长按顶栏。亮度、深色模式、待机、夜间时段、时钟和旋转与 Tessera 里一致，而且每一项都是 Home Assistant 里的实体。</sub></p>

## 在 Home Assistant 里管理

<p align="center">
  <img src="docs/images/editor-home.png" width="98%" alt="Tessera in Home Assistant: Your screens, seven screens from the 2.8-inch CYD to the 10.1-inch Guition, each with a preview of its first page drawn by its own firmware, one with an update waiting">
</p>
<p align="center">
  <img src="docs/images/editor.png" width="98%" alt="Tessera in Home Assistant: the living room screen's pages side by side, each with its title and top bar, Living room, Good morning, Comfort and Evening, and the library under them grouped by room">
</p>
<p align="center"><sub>Tessera 是 Home Assistant 里的一个面板：所有屏幕一目了然，选中屏幕的页面并排显示，实时呈现 Home Assistant 上报的数值，下方是你全家的实体库。</sub></p>
<p align="center">
  <img src="docs/images/editor-tiles.png" width="63%" alt="Choosing tiles: the pages of the screen side by side, and the library searched for lamp with the four lamps of the home and their rooms">
  <img src="docs/images/editor-tile-settings.png" width="33%" alt="Tile settings of the curtains in the drawer: on tap Perform action with Set cover position at 50 %, the position slider on the tile, the icon and the pastel background">
</p>
<p align="center"><sub>搜索你的家，把卡片拖到预览上，点按设置名称、宽度、控制和颜色，以及点按动作：打开详情卡、开关，或执行 Home Assistant 为它提供的任意动作，比如把窗帘开到 50 %。保存后屏幕即生效。⌘K 搜索屏幕、实体和动作；识别功能让屏幕闪烁，方便知道是哪一块。</sub></p>
<p align="center">
  <img src="docs/images/editor-top-bar.png" width="31%" alt="The top bar in the drawer: the page title on the left, and on the right the outdoor temperature, people at home and the time, with how each looks on the screen">
  <img src="docs/images/editor-settings.png" width="65%" alt="Settings in Tessera: New screen and Firmware & USB, the firmware updates, Language & region, the Alerts cheatsheet, and the Claude skill">
</p>
<p align="center"><sub>用你自己的家搭建的顶栏，通过 Wi-Fi 更新固件（愿意的话每晚自动），还有一个技能让 Claude 重新编排你的屏幕。</sub></p>
<p align="center">
  <img src="docs/images/editor-phone-screens.png" width="23%" alt="Tessera on a phone: Your screens, each with a preview of its first page drawn by its own firmware, one with an update waiting">
  <img src="docs/images/editor-phone-screen.png" width="23%" alt="One screen on a phone: its page as the screen shows it, the page picker under it and one big Add tile button">
  <img src="docs/images/editor-phone-tile.png" width="23%" alt="A tile tapped on a phone: a sheet with its icon and pastel background, More settings, Move and Remove">
  <img src="docs/images/editor-phone-add.png" width="23%" alt="Add tile on a phone: a sheet with search, the kinds as chips and the home's devices by room, each with a plus">
</p>
<p align="center"><sub>在手机上，Tessera 是日常修改的编辑器：你的屏幕、按屏幕样子显示的页面、点卡片改图标和颜色，以及添加卡片。其余都在屏幕的 ··· 菜单里，那里的<b>完整编辑器</b>可打开全部编辑功能。</sub></p>
<p align="center">
  <img src="docs/images/editor-screen-settings.png" width="98%" alt="The Screen settings tab in Tessera: Brightness with Dark mode and standby, Night with its hours and brightness, and Screen with back to Home, swiping, the page buttons and the rotation">
</p>
<p align="center"><sub>屏幕设置立即生效；在屏幕上或用自动化做的更改也会同步显示在这里。</sub></p>
<p align="center">
  <img src="docs/images/editor-override-yaml.png" width="50%" alt="Override YAML for the living room screen: a small file of its own, loaded after the shared package, here with the example that changes the display controller">
</p>
<p align="center"><sub>板上有别的硬件？CYD 的另一种显示控制器在新屏幕向导里就是一项选择；其他情况每块屏幕都有自己的覆盖 YAML，构建前由 ESPHome 检查，并在每次更新中保留。</sub></p>

## 用你的语言

<p align="center">
  <img src="docs/images/guition-german.png" width="31%" alt="A Guition in German: Wohnzimmer at the top with 16,8 °C, Dienstag, 15. September beside the analog clock, the days Di Mi Do, the Tischlampe at 75 % and Sam Zuhause">
  <img src="docs/images/guition-french.png" width="31%" alt="The same screen in French: Salon, mardi 15 septembre beside the clock, Éclaircies with the days ma me je, the Lampe de table at 75 % and Sam Maison">
  <img src="docs/images/guition-polish.png" width="31%" alt="The same screen in Polish: Salon, wtorek, 15 września beside the clock, the days wt śr cz, the Lampa stołowa at 75% and Sam w domu">
</p>
<p align="center"><sub>同一个家在德语、法语和波兰语下，房间和卡片都按各自语言命名。屏幕跟随你的 Home Assistant：它的语言、灯或扫地机器人的说法，以及你的国家书写日期、时间和数字的方式：德语法语是 75 %，波兰语和英语是 75%。</sub></p>


<p align="center">
  <img src="docs/images/editor-language.png" width="36%" alt="Language and region in Tessera: the screen language set to Home Assistant's language, the time format on 24 hour and the number format following the language">
</p>
<p align="center"><sub>想要与 Home Assistant 不同的语言时，到 设置 → 语言与地区 里改。</sub></p>

- **编辑器**跟随你 Home Assistant 资料的语言，家里两个人可以各看各的。
- **屏幕**在固件里内置一种语言：更改后按屏幕上的**更新**（或让夜间自动更新完成）。时钟（24 小时或 12 小时 AM/PM）和数字格式会立即在所有屏幕上同时改变。
  every screen at once.
- **Home Assistant 的措辞仍是 Home Assistant 的**：门、空调或机器人在卡片和详情里的说法，就是它自己仪表盘在你语言下的说法。


## 警报

<p align="center">
  <img src="docs/images/guition-alert-camera.png" width="41%" alt="An alert on the Guition with the front door camera's picture across the top: someone is at the door, with a Coming button">
  <img src="docs/images/guition-camera.png" width="41%" alt="The front door camera full screen on the Guition, with the round back key and the camera's name at the top">
</p>
<p align="center"><sub>有人到门口？自动化里的一条事件就能唤醒所有屏幕并显示。加上门铃摄像头，Guition 会告诉你是谁；点画面或摄像头卡片即可全屏查看，画面每几秒刷新。<a href="docs/CAMERA.md">摄像头画面</a>。</sub></p>
<p align="center">
  <img src="docs/images/guition-alert-choice-colors.png" width="41%" alt="An alert on the Guition asking to open the garage, with a red Decline and a green Accept button side by side">
  <img src="docs/images/editor-alerts.png" width="53%" alt="The Alerts cheatsheet in Tessera: a preview of the alert, a form to try one, and the action name of every screen, ready to copy">
</p>
<p align="center"><sub>任意警报，可发一块屏或全部屏，用你选的淡彩底色，一个或两个按钮可选，各有各的颜色和动作。<a href="README_EXTENDED.md#alert-from-an-automation">警报的工作方式</a>。自动化还可以把某个页面顶到最前，比如音乐响起时把整页播放器顶上来：<a href="README_EXTENDED.md#open-a-page-from-an-automation">用自动化打开页面</a>。</sub></p>

## 从 Home Assistant 安装

### 选哪块屏幕

| 屏幕 | 分辨率 | 显示 / 触摸 |
| --- | --- | --- |
| [CYD ESP32-2432S028](https://tessera-maxgramser.on-forge.com/screens/cyd) | 320 × 240，2 × 3 卡 | ILI9341 / 电阻式 XPT2046 |
| CYD ESP32-2432S028（ILI9342 版，实验性） | 320 × 240，2 × 3 卡 | ILI9342 / 电阻式 XPT2046；硬件验收待完成 |
| [Guition ESP32-S3-4848S040](https://tessera-maxgramser.on-forge.com/screens/guition)，4 英寸 | 480 × 480，2 × 3 卡 | ST7701S RGB / 电容式 GT911 |
| [Waveshare ESP32-S3-Touch-LCD-4.3](https://tessera-maxgramser.on-forge.com/screens/waveshare43) | 800 × 480，3 × 3 卡 | ST7262 RGB / 电容式 GT911（背光常亮：无待机、无夜间模式） |
| Waveshare ESP32-S3-Touch-LCD-5（较新） | 800 × 480，3 × 3 卡 | RGB / 电容式 GT911，4.3 英寸同款板配 5 英寸玻璃（背光常亮：无待机、无夜间模式；[详情](docs/WAVESHARE5.md)） |
| Guition JC8048W550C_I，5 英寸（实验性） | 800 × 480，3 × 3 卡 | ST7262 RGB / 电容式 GT911；背光可调，仅电容触控版本（[详情](docs/JC8048W550.md)） |
| [Waveshare ESP32-S3-Touch-LCD-7](https://tessera-maxgramser.on-forge.com/screens/waveshare7)（实验性） | 800 × 480，4 × 4 卡 | RGB / 电容式 GT911；背光常亮，硬件验收待完成（[详情](docs/WAVESHARE7.md)） |
| Waveshare ESP32-S3-Touch-LCD-7B（实验性） | 1024 × 600，4 × 4 卡 | RGB / 电容式 GT911；背光可调，硬件验收待完成（[详情](docs/WAVESHARE7B.md)） |
| Sunton ESP32-8048S070，7 英寸（实验性） | 800 × 480，4 × 4 卡 | RGB / 电容式 GT911；背光可调，硬件验收待完成（[详情](docs/SUNTON8048S070.md)） |
| [Waveshare ESP32-S3-Touch-LCD-4B](https://tessera-maxgramser.on-forge.com/screens/waveshare4b)，4 英寸（实验性） | 480 × 480，2 × 3 卡 | ST7701S RGB / 电容式 GT911；背光可调，硬件验收待完成（[详情](docs/WAVESHARE4B.md)） |
| [Waveshare ESP32-S3-Touch-LCD-3.5](https://tessera-maxgramser.on-forge.com/screens/waveshare35)（较新） | 480 × 320，2 × 2 卡 | ST7796 SPI / 电容式 FT6336；背光可调，无摄像头画面（[详情](docs/WAVESHARE35.md)） |
| [Hosyond ESP32-32E](https://tessera-maxgramser.on-forge.com/screens/hosyond40)，4 英寸（实验性） | 480 × 320，2 × 3 卡 | ST7796 SPI / 电阻式 XPT2046；背光可调，无摄像头画面，硬件验收待完成（[详情](docs/HOSYOND40.md)） |
| [Guition JC3248W535](docs/JC3248W535.md)，3.5 英寸（较新） | 480 × 320，2 × 2 卡 | AXS15231B QSPI / 电容式 AXS15231B；背光可调，支持摄像头画面 |
| [Guition JC8012P4A1](https://tessera-maxgramser.on-forge.com/screens/jc8012p4a1)，10.1 英寸 | 1280 × 800，5 × 5 卡 | MIPI-DSI JD9365 / 电容式 GSL3680，ESP32-P4（较新）（[详情](docs/JC8012P4A1.md)） |
| Guition JC8012P4A1 V2，10.1 英寸（实验性） | 1280 × 800，5 × 5 卡 | MIPI-DSI JD9365 / 电容式 GSL3680，早期 ESP32-P4 配新款 LCD；硬件验收待完成（[详情](docs/JC8012P4A1.md)） |
| Guition JC8012P4A1 V3，10.1 英寸（实验性） | 1280 × 800，5 × 5 卡 | MIPI-DSI JD9365 / 电容式 GSL3680，rev3 ESP32-P4；硬件验收待完成（[详情](docs/JC8012P4A1.md)） |
| [Waveshare ESP32-P4-86-Panel-ETH-2RO](docs/WAVESHAREP4.md)，4 英寸（实验性） | 720 × 720，2 × 3 卡 | MIPI-DSI ST7703 / 电容式 GT911，ESP32-P4；背光可调，仅 Wi-Fi（[详情](docs/WAVESHAREP4.md)） |
| Guition [JC1060P470](https://tessera-maxgramser.on-forge.com/screens/jc1060p470) 与 [JC1060P470 V2](https://tessera-maxgramser.on-forge.com/screens/jc1060p470v2)，7 英寸（实验性） | 1024 × 600，4 × 4 卡 | MIPI-DSI JD9165 / 电容式 GT911，ESP32-P4；硬件验收待完成（[详情](docs/JC1060P470.md)） |
| Guition JC4880P443，4.3 英寸（实验性） | 800 × 480，3 × 3 卡 | MIPI-DSI ST7701 / 电容式 GT911，pre-v3 ESP32-P4；背光可调（[详情](docs/JC4880P443.md)） |
| Elecrow CrowPanel Advanced 10.1 英寸，ESP32-P4（实验性） | 1024 × 600，5 × 5 卡 | MIPI-DSI EK79007 / 电容式 GT911，pre-v3 ESP32-P4，V1.1 或 V1.2；背光可调，带扬声器和麦克风（[详情](docs/CROWPANEL101.md)） |
| M5Stack Tab5（ST7121 版，较新） | 1280 × 720，3 × 3 卡 | MIPI-DSI ST7121 / 电容式 ST7121，ESP32-P4；硬件已实测（[详情](docs/TAB5.md)） |

每块屏幕都链接到 [Tessera 网站](https://tessera-maxgramser.on-forge.com/screens)上的页面，里面有使用者反馈的情况。

> **让你的屏幕跑起来了？告诉下一个人。**一块板值不值得买，只有用过的人知道。在网站的[我的屏幕实装](https://tessera-maxgramser.on-forge.com/community/share?type=installation)里记录你的确切板型、固件版本，以及显示、触摸和连接是否正常，每个账号每块板一条。只要一分钟（用 GitHub 登录），实验性的板子就是这样变成大家可以放心买的板子。有问题？在网站上[报告问题](https://tessera-maxgramser.on-forge.com/community/share?type=issue)，或在这里开 issue。

请使用这些确切的板型变体：名字相似的产品可能用不同的控制器或接口。Wallbox 的继电器默认不受控；带继电器的 4 英寸 Guition 可以通过它的覆盖 YAML 控制它们（[docs/GUITION.md](docs/GUITION.md#relays)）。

我们自己用的是 4 英寸 Guition，它一直表现不错：亮度足、触摸跟手，挂墙数月无一次故障。购买地址：[Guition ESP32-S3-4848S040（AliExpress）](https://nl.aliexpress.com/item/1005008506761923.html)。AliExpress 上的链接随时可能失效；失效时直接搜"ESP32-S3-4848S040"，下单前确认商品标注 480×480、ST7701S 和电容 GT911 触摸。
touch panel before you order.

Tessera 用自己的 **ESPHome 2026.9.0** 构建。固件也可以在你自己的 ESPHome Device Builder 里构建，要求 ESPHome 2026.6.2 或更新；10.1 英寸 Guition 要求 2026.8.0 或更新，因为它的触摸面板更新。
newer than that.

10.1 英寸 Guition 是**本版本的最新成员，尚未经过我们自己的验收测试**：硬件已经在真面板上推敲并烧录，屏幕软件在所有板子上又完全一致，但两者还没有在同一张桌上会过面。欢迎反馈。它需要 pre-v3 硅片的面板（启动日志显示 `chip revision: v1.3` 或其他低于 v3.0 的版本），这批面板目前出厂都是如此；rev3 硅片需要自己的固件。

### 需要单独装 ESPHome 吗？

**你不需要单独安装 ESPHome Device Builder 应用。**Tessera Screen Manager 已内置 ESPHome 命令行，可以自己构建固件、通过 USB 安装、从浏览器刷入接在你自己电脑上的屏幕，或给你固件文件，之后通过 OTA 无线更新。

**Home Assistant 里无需任何设置。**刚烧录的屏幕一连上你的 Wi-Fi，Tessera 就会用屏幕自己的密钥把它加进 Home Assistant 的 ESPHome 集成，并允许它执行 Home Assistant 动作——卡片要控制任何东西都靠这个。

| 组件 | 是否需要 | 用途 |
| --- | --- | --- |
| Tessera Screen Manager 应用 | 是，本安装路线必需 | 安装固件、管理卡片、向屏幕发送实时数据 |
| ESPHome Device Builder 应用 | 否，可选 | 另一个编辑器和固件安装器；同样的命令行已内置在 Tessera 中 |
| HA 中的 ESPHome 集成 | 是，Tessera 会自动把每块屏幕加入 | Home Assistant 与实体屏幕之间的连接 |

所以没有 ESPHome Device Builder 的全新安装也没问题。如果还没有 ESPHome 的 secrets.yaml，向导会只问一次 Wi-Fi 并保存在本地；已有的 Wi-Fi secrets 会被复用。API 和 OTA 密钥按新屏幕分别生成，保存在各自设备的配置里。

### 一步步来

Home Assistant Container（Docker）没有应用商店，请按照[用 Docker 安装](https://tessera-maxgramser.on-forge.com/docs/docker)操作。

有应用/插件的 Home Assistant OS（**aarch64 或 amd64**）：

1. Tessera 不在默认应用商店，先添加它的仓库。点一下就行：

   [![把 Tessera 仓库添加到你的 Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fshom%2Fhomeassistant_espscreen)

   或手动添加：打开应用商店，在右上角菜单选 **仓库**，添加
   `https://github.com/shom/homeassistant_espscreen`。
2. 从商店安装 **Tessera Screen Manager**，启动应用，在侧栏打开 **Tessera**。ESPHome Device Builder 是可选的：本应用已内置 ESPHome 命令行。
3. 用 USB 数据线把屏幕接到 **Home Assistant 主机**，点侧栏 Screens 旁的 **+**。新屏幕向导有三步：**屏幕**（选你的板型）、**设置**（起名并选择横竖朝向）、**安装**（选“USB 接 Home Assistant”并点**安装**）。如果 ESPHome 的 secrets.yaml 里缺 Wi-Fi，设置步骤会问一次，Tessera 只补缺的行。带唯一 API 和 OTA 密钥的配置会存入 ESPHome 文件夹；构建和烧录在同一个窗口进行（树莓派上首次构建需要几分钟）。每块屏幕都有自己的配置。Home Assistant 装在服务器或虚拟机里、屏幕够不着？把屏幕接到你自己的电脑，在安装步骤选**从这台电脑**：Tessera 构建固件，本页面在 Chrome 或 Edge（Home Assistant 需以 https 打开）里把固件刷入屏幕。或选**下载文件**，用 [ESPHome Web](https://web.esphome.io) 自己刷。之后更新照常走 Wi-Fi。
4. **CYD：**在屏幕上完成校准。**Guition：**使用 GT911，无需电阻式校准。屏幕加入你的 Wi-Fi 后会自动出现在 Tessera 里。
5. 在 Tessera 里选中屏幕、挑好卡片，点**保存并发送**。然后试试实体的按键和滑条。

<p align="center">
  <img src="docs/images/editor-new-screen.png" width="37%" alt="New screen in Tessera: the first of three steps, every supported board with its size, resolution and touch chip, the 4-inch Guition chosen">
  <img src="docs/images/editor-tiles.png" width="59%" alt="Choosing tiles: the pages of the screen side by side, and the library searched for lamp">
</p>
<p align="center"><sub>新屏幕的第一步（上面的第 3 步），以及挑选卡片（第 5 步）。</sub></p>

新固件通过 Tessera 里屏幕的**更新**按钮经 Wi-Fi 安装；在**设置**里打开后，也可每晚自动更新；侧栏的**固件与 USB → Wi-Fi / OTA** 可手动安装。对已有的屏幕，请始终使用已有的配置；新建安装配置会生成新密钥。
installation profile generates new keys.

网站上的[手册](https://tessera-maxgramser.on-forge.com/docs/install)会更详细地过一遍每个步骤。

## 更多

- **[Tessera 网站上的手册](https://tessera-maxgramser.on-forge.com/docs/)：**[安装](https://tessera-maxgramser.on-forge.com/docs/install)、[页面](https://tessera-maxgramser.on-forge.com/docs/pages)、[卡片](https://tessera-maxgramser.on-forge.com/docs/tiles)、[屏幕设置](https://tessera-maxgramser.on-forge.com/docs/screen-settings)、[摄像头](https://tessera-maxgramser.on-forge.com/docs/cameras)、[Docker](https://tessera-maxgramser.on-forge.com/docs/docker)与[疑难解答](https://tessera-maxgramser.on-forge.com/docs/troubleshooting)。
- **[完整参考](README_EXTENDED.md)：**每张卡片和每个设置、来自自动化的警报与唤醒/睡眠、顶栏、屏幕上的设置页，以及更新如何保留你的设置。
- [Guition 硬件、安装与旋转](docs/GUITION.md) ·
  [CYD 校准与 USB 诊断](docs/CALIBRATING.md) ·
  [发布历史](screen_manager/CHANGELOG.md)
  [Release history](screen_manager/CHANGELOG.md)

## 致谢与许可

ESP Screens 的灵感来自 Adrian Kuehlewind 的 [ESPHome-touch-display-mount](https://github.com/akuehlewind/ESPHome-touch-display-mount)，最初的版本从他的代码起步。项目后来走出了自己的路，但他的仓库仍然是给 CYD 一个好归宿的去处：有漂亮的 3D 打印桌面、桌下、壁挂和嵌入式支架。
wall and flush mounts.

别与 [Tesserae（tesserae.ink）](https://tesserae.ink)混淆——那是一个独立的开源项目，为 Home Assistant 的 e-ink 面板制作安静的信息面板。同一个词，不同的屏：Tessera 面向彩色 LCD 触摸屏，Tesserae 面向电子墨水。找错门的提问我们也很乐意转达。

摄像头图片里的前门是一张照片，来自 Unsplash 上的 [Virginia Marinova](https://unsplash.com/photos/the-door-welcomes-with-plants-on-both-sides-80uwJgdeqWg)。

Tessera（原 ESP Screens）基于 GNU Affero General Public License v3.0 许可发布，见 [LICENSE](LICENSE) 与 [NOTICE](NOTICE)。0.4.38 及之前的版本为 MIT 许可，且保持不变。
