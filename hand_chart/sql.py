# SQL запросы

SQL_GET_STACKS_BY_ACTION = """
SELECT hand_chart_contenthandchart.table_id
FROM hand_chart_contenthandchart
    JOIN hand_chart_contenthandchart_utg utg ON hand_chart_contenthandchart.id = utg.contenthandchart_id
    JOIN hand_chart_contenthandchart_utg1 utg1 ON hand_chart_contenthandchart.id = utg1.contenthandchart_id
    JOIN hand_chart_contenthandchart_mp mp ON hand_chart_contenthandchart.id = mp.contenthandchart_id
    JOIN hand_chart_contenthandchart_mp1 mp1 ON hand_chart_contenthandchart.id = mp1.contenthandchart_id
    JOIN hand_chart_contenthandchart_hj hj ON hand_chart_contenthandchart.id = hj.contenthandchart_id
    JOIN hand_chart_contenthandchart_co co ON hand_chart_contenthandchart.id = co.contenthandchart_id
    JOIN hand_chart_contenthandchart_btn btn ON hand_chart_contenthandchart.id = btn.contenthandchart_id
    JOIN hand_chart_contenthandchart_sb sb ON hand_chart_contenthandchart.id = sb.contenthandchart_id
WHERE utg.optionsaction_id = %s OR utg1.optionsaction_id = %s  OR mp.optionsaction_id = %s  OR mp1.optionsaction_id = %s
    or hj.optionsaction_id = %s OR co.optionsaction_id = %s OR btn.optionsaction_id = %s OR sb.optionsaction_id = %s
GROUP BY hand_chart_contenthandchart.table_id
"""


SQL_GET_ACTION_IDS_BY_STACK = """
SELECT utg.color_id, utg1.color_id, mp.color_id, mp1.color_id, hl.color_id, co.color_id, btn.color_id, sb.color_id
FROM hand_chart_tablehandchart
    JOIN hand_chart_contenthandchart on hand_chart_contenthandchart.table_id=hand_chart_tablehandchart.id
    JOIN hand_chart_contenthandchart_utg utg on hand_chart_contenthandchart.id = utg.contenthandchart_id
    JOIN hand_chart_contenthandchart_utg1 utg1 on hand_chart_contenthandchart.id = utg1.contenthandchart_id
    JOIN hand_chart_contenthandchart_mp mp on hand_chart_contenthandchart.id = mp.contenthandchart_id
    JOIN hand_chart_contenthandchart_mp1 mp1 on hand_chart_contenthandchart.id = mp1.contenthandchart_id
    JOIN hand_chart_contenthandchart_hj hj on hand_chart_contenthandchart.id = hj.contenthandchart_id
    JOIN hand_chart_contenthandchart_co co on hand_chart_contenthandchart.id = co.contenthandchart_id
    JOIN hand_chart_contenthandchart_btn btn on hand_chart_contenthandchart.id = btn.contenthandchart_id
    JOIN hand_chart_contenthandchart_sb sb on hand_chart_contenthandchart.id = sb.contenthandchart_id
WHERE hand_chart_tablehandchart.stack_id=%s
"""