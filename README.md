# 🌍 上海环境能源交易所 - 碳配额行情数据

实时展示上海环境能源交易所（SEEEX）碳配额交易数据。

## 📊 功能特性

- ✅ 实时价格展示（最新价、开盘价、最高价、最低价）
- ✅ 价格走势图（最近 7-14 天历史数据）
- ✅ 市场概况（成交量、成交额、涨跌幅）
- ✅ 最新动态/新闻
- ✅ 自动每日更新（GitHub Actions）
- ✅ 响应式设计（支持手机/平板/桌面）

## 🚀 部署到 GitHub Pages

### 方法 1：使用 GitHub Actions（推荐）

1. **创建新仓库**
   ```bash
   # 在 GitHub 上创建新仓库，例如：shanghai-emission-exchange
   ```

2. **推送代码**
   ```bash
   cd shanghai-emission-exchange
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/你的用户名/shanghai-emission-exchange.git
   git push -u origin main
   ```

3. **启用 GitHub Pages**
   - 进入仓库 → Settings → Pages
   - Source 选择 `main` 分支
   - 保存后等待部署完成

4. **启用自动更新**
   - GitHub Actions 会自动在每个交易日 15:30 更新数据
   - 也可以手动触发：Actions → Update Market Data → Run workflow

### 方法 2：手动部署

1. 将 `index.html` 和 `data.json` 上传到 GitHub 仓库
2. 启用 GitHub Pages
3. 手动更新 `data.json` 数据

## 📁 项目结构

```
shanghai-emission-exchange/
├── index.html              # 主页面
├── data.json               # 市场数据（自动更新）
├── README.md               # 项目说明
├── .github/
│   └── workflows/
│       └── update-data.yml # GitHub Actions 工作流
└── scripts/
    └── fetch_data.py       # 数据抓取脚本
```

## 🔧 自定义

### 修改更新频率

编辑 `.github/workflows/update-data.yml`：

```yaml
on:
  schedule:
    - cron: '30 7 * * 1-5'  # 每周一至周五 15:30 (UTC+8)
```

### 添加更多数据字段

修改 `scripts/fetch_data.py` 中的 `fetch_market_data()` 函数。

## 📝 数据来源

- 官方网站：https://www.cneeex.com/
- 数据更新频率：每个交易日 15:30

## ⚠️ 免责声明

本网站展示的数据仅供参考，不构成投资建议。实际交易数据以上海环境能源交易所官方公布为准。

## 📄 License

MIT License
