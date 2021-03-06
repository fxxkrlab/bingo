# Inline Content Template

INLINE_MOVIE_STR = """
• <b>原片名 :</b> {}
• <b>地区译名 :</b> {}
• <b>上映时间 :</b> {}
• <b>人气度 :</b> {}
• <b>语言 :</b> {}
• <b>平均得分 :</b> {}

• <b>简介 :</b> {}
"""

INLINE_TV_STR = """
• <b>原片名 :</b> {}
• <b>地区译名 :</b> {}
• <b>国家/地区 :</b> {}
• <b>首播时间 :</b> {}
• <b>人气度 :</b> {}
• <b>语言 :</b> {}
• <b>平均得分 :</b> {}

• <b>简介 :</b> {}
"""

INLINE_FORMAT_NOTICE = """
<pre>• InlineQuery •</pre>
<b>命令格式提示</b>
<b>请按照以下格式查询</b>
------------------------------
<pre>movie 电影名 y:年份(可选参数)</pre>
<pre>tv 电视剧名 y:年份(可选参数)</pre>
------------------------------
<pre>e.g. movie 钢铁侠</pre>
<pre>e.g. movie 钢铁侠 y:2013</pre>
"""