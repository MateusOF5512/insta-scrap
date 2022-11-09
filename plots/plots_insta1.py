import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
import requests



def requi(perfil):
    url = f"https://instagram204.p.rapidapi.com/userinfo/{perfil}"
    headers = {
        "X-RapidAPI-Key": "aaa93512camsh8984e550bc12f2ap146296jsne961f7a1b8f7",
        "X-RapidAPI-Host": "instagram204.p.rapidapi.com"
    }

    res = requests.request("GET", url, headers=headers).json()

    return res


def convert_csv1(res):
    ex_url = res["data"]["external_url"]
    seguidores = res["data"]["edge_followed_by"]['count']
    seguindo = res["data"]["edge_follow"]['count']
    midia = res["data"]["edge_owner_to_timeline_media"]["count"]
    video = res["data"]["edge_felix_video_timeline"]["count"]
    userid = res["data"]["id"]
    business = res["data"]["is_business_account"]
    profissional = res["data"]["is_professional_account"]
    privado = res["data"]["is_private"]
    transparente = res["data"]["is_eligible_to_view_account_transparency"]
    cat_nome = res["data"]["business_category_name"]
    busi_nome = res["data"]["category_name"]
    foto = res["data"]["profile_pic_url_hd"]

    dados = {'seguidores': seguidores, 'seguindo': seguindo, 'midia': midia, 'video': video,
             'userid': userid, 'business': business, 'profissional':profissional,
             'privado':privado, 'transparente': transparente, 'cat_nome': cat_nome,
             'busi_nome': busi_nome, 'foto': foto, 'ex_url': ex_url}
    dados = pd.DataFrame([dados])

    return dados

def convert_csv_midia(res):
    try:
        df0m = res["data"]["edge_owner_to_timeline_media"]['edges'][0]['node']
        df1m = res["data"]["edge_owner_to_timeline_media"]['edges'][1]['node']
        df2m = res["data"]["edge_owner_to_timeline_media"]['edges'][2]['node']
        df3m = res["data"]["edge_owner_to_timeline_media"]['edges'][3]['node']
        df4m = res["data"]["edge_owner_to_timeline_media"]['edges'][4]['node']
        df5m = res["data"]["edge_owner_to_timeline_media"]['edges'][5]['node']
        df6m = res["data"]["edge_owner_to_timeline_media"]['edges'][6]['node']
        df7m = res["data"]["edge_owner_to_timeline_media"]['edges'][7]['node']
        df8m = res["data"]["edge_owner_to_timeline_media"]['edges'][8]['node']
        df9m = res["data"]["edge_owner_to_timeline_media"]['edges'][9]['node']
        df10m = res["data"]["edge_owner_to_timeline_media"]['edges'][10]['node']
        df11m = res["data"]["edge_owner_to_timeline_media"]['edges'][11]['node']

        df0_1 = df0m["edge_media_to_comment"]['count']; df0_1 = pd.DataFrame([df0_1])
        df0_2 = df0m["edge_liked_by"]['count']; df0_2 = pd.DataFrame([df0_2])
        df0_3 = df0m["edge_media_to_caption"]['edges'][0]['node']['text']; df0_3 = pd.DataFrame([df0_3])

        df1_1 = df1m["edge_media_to_comment"]['count']; df1_1 = pd.DataFrame([df1_1])
        df1_2 = df1m["edge_liked_by"]['count']; df1_2 = pd.DataFrame([df1_2])
        df1_3 = df1m["edge_media_to_caption"]['edges'][0]['node']['text']; df1_3 = pd.DataFrame([df1_3])

        df2_1 = df2m["edge_media_to_comment"]['count']; df2_1 = pd.DataFrame([df2_1])
        df2_2 = df2m["edge_liked_by"]['count']; df2_2 = pd.DataFrame([df2_2])
        df2_3 = df2m["edge_media_to_caption"]['edges'][0]['node']['text']; df2_3 = pd.DataFrame([df2_3])

        df3_1 = df3m["edge_media_to_comment"]['count']; df3_1 = pd.DataFrame([df3_1])
        df3_2 = df3m["edge_liked_by"]['count']; df3_2 = pd.DataFrame([df3_2])
        df3_3 = df3m["edge_media_to_caption"]['edges'][0]['node']['text']; df3_3 = pd.DataFrame([df3_3])

        df4_1 = df4m["edge_media_to_comment"]['count']; df4_1 = pd.DataFrame([df4_1])
        df4_2 = df4m["edge_liked_by"]['count']; df4_2 = pd.DataFrame([df4_2])
        df4_3 = df4m["edge_media_to_caption"]['edges'][0]['node']['text']; df4_3 = pd.DataFrame([df4_3])

        df5_1 = df5m["edge_media_to_comment"]['count']; df5_1 = pd.DataFrame([df5_1])
        df5_2 = df5m["edge_liked_by"]['count']; df5_2 = pd.DataFrame([df5_2])
        df5_3 = df5m["edge_media_to_caption"]['edges'][0]['node']['text']; df5_3 = pd.DataFrame([df5_3])

        df6_1 = df6m["edge_media_to_comment"]['count']; df6_1 = pd.DataFrame([df6_1])
        df6_2 = df6m["edge_liked_by"]['count']; df6_2 = pd.DataFrame([df6_2])
        df6_3 = df6m["edge_media_to_caption"]['edges'][0]['node']['text']; df6_3 = pd.DataFrame([df6_3])

        df7_1 = df7m["edge_media_to_comment"]['count']; df7_1 = pd.DataFrame([df7_1])
        df7_2 = df7m["edge_liked_by"]['count']; df7_2 = pd.DataFrame([df7_2])
        df7_3 = df7m["edge_media_to_caption"]['edges'][0]['node']['text']; df7_3 = pd.DataFrame([df7_3])

        df8_1 = df8m["edge_media_to_comment"]['count']; df8_1 = pd.DataFrame([df8_1])
        df8_2 = df8m["edge_liked_by"]['count']; df8_2 = pd.DataFrame([df8_2])
        df8_3 = df8m["edge_media_to_caption"]['edges'][0]['node']['text']; df8_3 = pd.DataFrame([df8_3])

        df9_1 = df9m["edge_media_to_comment"]['count']; df9_1 = pd.DataFrame([df9_1])
        df9_2 = df9m["edge_liked_by"]['count']; df9_2 = pd.DataFrame([df9_2])
        df9_3 = df9m["edge_media_to_caption"]['edges'][0]['node']['text']; df9_3 = pd.DataFrame([df9_3])

        df10_1 = df10m["edge_media_to_comment"]['count']; df10_1 = pd.DataFrame([df10_1])
        df10_2 = df10m["edge_liked_by"]['count']; df10_2 = pd.DataFrame([df10_2])
        df10_3 = df10m["edge_media_to_caption"]['edges'][0]['node']['text']; df10_3 = pd.DataFrame([df10_3])

        df11_1 = df11m["edge_media_to_comment"]['count']; df11_1 = pd.DataFrame([df11_1])
        df11_2 = df11m["edge_liked_by"]['count']; df11_2 = pd.DataFrame([df11_2])
        df11_3 = df11m["edge_media_to_caption"]['edges'][0]['node']['text']; df11_3 = pd.DataFrame([df11_3])

        df0m = pd.DataFrame([df0m])
        df1m = pd.DataFrame([df1m])
        df2m = pd.DataFrame([df2m])
        df3m = pd.DataFrame([df3m])
        df4m = pd.DataFrame([df4m])
        df5m = pd.DataFrame([df5m])
        df6m = pd.DataFrame([df6m])
        df7m = pd.DataFrame([df7m])
        df8m = pd.DataFrame([df8m])
        df9m = pd.DataFrame([df9m])
        df10m = pd.DataFrame([df10m])
        df11m = pd.DataFrame([df11m])

        df0_ = pd.concat([df0m, df0_1, df0_2, df0_3], axis=1)
        df1_ = pd.concat([df1m, df1_1, df1_2, df1_3], axis=1)
        df2_ = pd.concat([df2m, df2_1, df2_2, df2_3], axis=1)
        df3_ = pd.concat([df3m, df3_1, df3_2, df3_3], axis=1)
        df4_ = pd.concat([df4m, df4_1, df4_2, df4_3], axis=1)
        df5_ = pd.concat([df5m, df5_1, df5_2, df5_3], axis=1)
        df6_ = pd.concat([df6m, df6_1, df6_2, df6_3], axis=1)
        df7_ = pd.concat([df7m, df7_1, df7_2, df7_3], axis=1)
        df8_ = pd.concat([df8m, df8_1, df8_2, df8_3], axis=1)
        df9_ = pd.concat([df9m, df9_1, df9_2, df9_3], axis=1)
        df10_ = pd.concat([df10m, df10_1, df10_2, df10_3], axis=1)
        df11_ = pd.concat([df11m, df11_1, df11_2, df11_3], axis=1)

        df0_.columns.values[-3] = "COMENTARIOS"
        df0_.columns.values[-2] = "LIKES"
        df0_.columns.values[-1] = "TEXTO"

        df1_.columns.values[-3] = "COMENTARIOS"
        df1_.columns.values[-2] = "LIKES"
        df1_.columns.values[-1] = "TEXTO"

        df2_.columns.values[-3] = "COMENTARIOS"
        df2_.columns.values[-2] = "LIKES"
        df2_.columns.values[-1] = "TEXTO"

        df3_.columns.values[-3] = "COMENTARIOS"
        df3_.columns.values[-2] = "LIKES"
        df3_.columns.values[-1] = "TEXTO"

        df4_.columns.values[-3] = "COMENTARIOS"
        df4_.columns.values[-2] = "LIKES"
        df4_.columns.values[-1] = "TEXTO"

        df5_.columns.values[-3] = "COMENTARIOS"
        df5_.columns.values[-2] = "LIKES"
        df5_.columns.values[-1] = "TEXTO"

        df6_.columns.values[-3] = "COMENTARIOS"
        df6_.columns.values[-2] = "LIKES"
        df6_.columns.values[-1] = "TEXTO"

        df7_.columns.values[-3] = "COMENTARIOS"
        df7_.columns.values[-2] = "LIKES"
        df7_.columns.values[-1] = "TEXTO"

        df8_.columns.values[-3] = "COMENTARIOS"
        df8_.columns.values[-2] = "LIKES"
        df8_.columns.values[-1] = "TEXTO"

        df9_.columns.values[-3] = "COMENTARIOS"
        df9_.columns.values[-2] = "LIKES"
        df9_.columns.values[-1] = "TEXTO"

        df10_.columns.values[-3] = "COMENTARIOS"
        df10_.columns.values[-2] = "LIKES"
        df10_.columns.values[-1] = "TEXTO"

        df11_.columns.values[-3] = "COMENTARIOS"
        df11_.columns.values[-2] = "LIKES"
        df11_.columns.values[-1] = "TEXTO"

        dfm = pd.concat([df0_, df1_, df2_, df3_, df4_, df5_, df6_, df7_, df8_, df9_, df10_, df11_], axis=0)

        dfm['TIME'] = [datetime.fromtimestamp(x) for x in dfm['taken_at_timestamp']]

        dfm = dfm[['__typename', 'LIKES', 'COMENTARIOS',
                   'TEXTO', 'TIME', 'location', 'shortcode', 'id']]

        dfm = dfm.rename(columns={'__typename': 'TIPO POST', 'location': 'LOCALIZAÇAO',
                                  'shortcode':'SHORTLINK', 'id':'ID POST'})

    except:
        d = {'nome': [res], 'status': ['ERRO']}
        dfm = pd.DataFrame(d)

    return dfm



def convert_csv_video(res):
    try:
        df0v = res["data"]["edge_felix_video_timeline"]['edges'][0]['node']
        df1v = res["data"]["edge_felix_video_timeline"]['edges'][1]['node']
        df2v = res["data"]["edge_felix_video_timeline"]['edges'][2]['node']
        df3v = res["data"]["edge_felix_video_timeline"]['edges'][3]['node']
        df4v = res["data"]["edge_felix_video_timeline"]['edges'][4]['node']
        df5v = res["data"]["edge_felix_video_timeline"]['edges'][5]['node']
        df6v = res["data"]["edge_felix_video_timeline"]['edges'][6]['node']
        df7v = res["data"]["edge_felix_video_timeline"]['edges'][7]['node']
        df8v = res["data"]["edge_felix_video_timeline"]['edges'][8]['node']
        df9v = res["data"]["edge_felix_video_timeline"]['edges'][9]['node']
        df10v = res["data"]["edge_felix_video_timeline"]['edges'][10]['node']
        df11v = res["data"]["edge_felix_video_timeline"]['edges'][11]['node']

        df0_1 = df0v["edge_media_to_comment"]['count'];df0_1 = pd.DataFrame([df0_1])
        df0_2 = df0v["edge_liked_by"]['count']; df0_2 = pd.DataFrame([df0_2])
        df0_3 = df0v["edge_media_to_caption"]['edges'][0]['node']['text']; df0_3 = pd.DataFrame([df0_3])

        df1_1 = df1v["edge_media_to_comment"]['count']; df1_1 = pd.DataFrame([df1_1])
        df1_2 = df1v["edge_liked_by"]['count']; df1_2 = pd.DataFrame([df1_2])
        df1_3 = df1v["edge_media_to_caption"]['edges'][0]['node']['text']; df1_3 = pd.DataFrame([df1_3])

        df2_1 = df2v["edge_media_to_comment"]['count']; df2_1 = pd.DataFrame([df2_1])
        df2_2 = df2v["edge_liked_by"]['count']; df2_2 = pd.DataFrame([df2_2])
        df2_3 = df2v["edge_media_to_caption"]['edges'][0]['node']['text']; df2_3 = pd.DataFrame([df2_3])

        df3_1 = df3v["edge_media_to_comment"]['count']; df3_1 = pd.DataFrame([df3_1])
        df3_2 = df3v["edge_liked_by"]['count']; df3_2 = pd.DataFrame([df3_2])
        df3_3 = df3v["edge_media_to_caption"]['edges'][0]['node']['text']; df3_3 = pd.DataFrame([df3_3])

        df4_1 = df4v["edge_media_to_comment"]['count']; df4_1 = pd.DataFrame([df4_1])
        df4_2 = df4v["edge_liked_by"]['count']; df4_2 = pd.DataFrame([df4_2])
        df4_3 = df4v["edge_media_to_caption"]['edges'][0]['node']['text']; df4_3 = pd.DataFrame([df4_3])

        df5_1 = df5v["edge_media_to_comment"]['count']; df5_1 = pd.DataFrame([df5_1])
        df5_2 = df5v["edge_liked_by"]['count']; df5_2 = pd.DataFrame([df5_2])
        df5_3 = df5v["edge_media_to_caption"]['edges'][0]['node']['text']; df5_3 = pd.DataFrame([df5_3])

        df6_1 = df6v["edge_media_to_comment"]['count']; df6_1 = pd.DataFrame([df6_1])
        df6_2 = df6v["edge_liked_by"]['count']; df6_2 = pd.DataFrame([df6_2])
        df6_3 = df6v["edge_media_to_caption"]['edges'][0]['node']['text']; df6_3 = pd.DataFrame([df6_3])

        df7_1 = df7v["edge_media_to_comment"]['count']; df7_1 = pd.DataFrame([df7_1])
        df7_2 = df7v["edge_liked_by"]['count']; df7_2 = pd.DataFrame([df7_2])
        df7_3 = df7v["edge_media_to_caption"]['edges'][0]['node']['text']; df7_3 = pd.DataFrame([df7_3])

        df8_1 = df8v["edge_media_to_comment"]['count']; df8_1 = pd.DataFrame([df8_1])
        df8_2 = df8v["edge_liked_by"]['count']; df8_2 = pd.DataFrame([df8_2])
        df8_3 = df8v["edge_media_to_caption"]['edges'][0]['node']['text']; df8_3 = pd.DataFrame([df8_3])

        df9_1 = df9v["edge_media_to_comment"]['count']; df9_1 = pd.DataFrame([df9_1])
        df9_2 = df9v["edge_liked_by"]['count']; df9_2 = pd.DataFrame([df9_2])
        df9_3 = df9v["edge_media_to_caption"]['edges'][0]['node']['text']; df9_3 = pd.DataFrame([df9_3])

        df10_1 = df10v["edge_media_to_comment"]['count']; df10_1 = pd.DataFrame([df10_1])
        df10_2 = df10v["edge_liked_by"]['count']; df10_2 = pd.DataFrame([df10_2])
        df10_3 = df10v["edge_media_to_caption"]['edges'][0]['node']['text']; df10_3 = pd.DataFrame([df10_3])

        df11_1 = df11v["edge_media_to_comment"]['count']; df11_1 = pd.DataFrame([df11_1])
        df11_2 = df11v["edge_liked_by"]['count']; df11_2 = pd.DataFrame([df11_2])
        df11_3 = df11v["edge_media_to_caption"]['edges'][0]['node']['text']; df11_3 = pd.DataFrame([df11_3])

        df0v = pd.DataFrame([df0v])
        df1v = pd.DataFrame([df1v])
        df2v = pd.DataFrame([df2v])
        df3v = pd.DataFrame([df3v])
        df4v = pd.DataFrame([df4v])
        df5v = pd.DataFrame([df5v])
        df6v = pd.DataFrame([df6v])
        df7v = pd.DataFrame([df7v])
        df8v = pd.DataFrame([df8v])
        df9v = pd.DataFrame([df9v])
        df10v = pd.DataFrame([df10v])
        df11v = pd.DataFrame([df11v])

        df0_ = pd.concat([df0v, df0_1, df0_2, df0_3], axis=1)
        df1_ = pd.concat([df1v, df1_1, df1_2, df1_3], axis=1)
        df2_ = pd.concat([df2v, df2_1, df2_2, df2_3], axis=1)
        df3_ = pd.concat([df3v, df3_1, df3_2, df3_3], axis=1)
        df4_ = pd.concat([df4v, df4_1, df4_2, df4_3], axis=1)
        df5_ = pd.concat([df5v, df5_1, df5_2, df5_3], axis=1)
        df6_ = pd.concat([df6v, df6_1, df6_2, df6_3], axis=1)
        df7_ = pd.concat([df7v, df7_1, df7_2, df7_3], axis=1)
        df8_ = pd.concat([df8v, df8_1, df8_2, df8_3], axis=1)
        df9_ = pd.concat([df9v, df9_1, df9_2, df9_3], axis=1)
        df10_ = pd.concat([df10v, df10_1, df10_2, df10_3], axis=1)
        df11_ = pd.concat([df11v, df11_1, df11_2, df11_3], axis=1)

        df0_.columns.values[-3] = "COMENTARIOS"
        df0_.columns.values[-2] = "LIKES"
        df0_.columns.values[-1] = "TEXTO"

        df1_.columns.values[-3] = "COMENTARIOS"
        df1_.columns.values[-2] = "LIKES"
        df1_.columns.values[-1] = "TEXTO"

        df2_.columns.values[-3] = "COMENTARIOS"
        df2_.columns.values[-2] = "LIKES"
        df2_.columns.values[-1] = "TEXTO"

        df3_.columns.values[-3] = "COMENTARIOS"
        df3_.columns.values[-2] = "LIKES"
        df3_.columns.values[-1] = "TEXTO"

        df4_.columns.values[-3] = "COMENTARIOS"
        df4_.columns.values[-2] = "LIKES"
        df4_.columns.values[-1] = "TEXTO"

        df5_.columns.values[-3] = "COMENTARIOS"
        df5_.columns.values[-2] = "LIKES"
        df5_.columns.values[-1] = "TEXTO"

        df6_.columns.values[-3] = "COMENTARIOS"
        df6_.columns.values[-2] = "LIKES"
        df6_.columns.values[-1] = "TEXTO"

        df7_.columns.values[-3] = "COMENTARIOS"
        df7_.columns.values[-2] = "LIKES"
        df7_.columns.values[-1] = "TEXTO"

        df8_.columns.values[-3] = "COMENTARIOS"
        df8_.columns.values[-2] = "LIKES"
        df8_.columns.values[-1] = "TEXTO"

        df9_.columns.values[-3] = "COMENTARIOS"
        df9_.columns.values[-2] = "LIKES"
        df9_.columns.values[-1] = "TEXTO"

        df10_.columns.values[-3] = "COMENTARIOS"
        df10_.columns.values[-2] = "LIKES"
        df10_.columns.values[-1] = "TEXTO"

        df11_.columns.values[-3] = "COMENTARIOS"
        df11_.columns.values[-2] = "LIKES"
        df11_.columns.values[-1] = "TEXTO"

        dfv = pd.concat([df0_, df1_, df2_, df3_, df4_, df5_, df6_, df7_, df8_, df9_, df10_, df11_], axis=0)

        dfv['TIME'] = [datetime.fromtimestamp(x) for x in dfv['taken_at_timestamp']]

        dfv = dfv[['product_type', '__typename','video_view_count', 'LIKES', 'COMENTARIOS',
                   'TEXTO', 'video_duration', 'TIME', 'location', 'shortcode', 'id']]

        dfv = dfv.rename(columns={'product_type':'TIPO PRODUTO', '__typename': 'TIPO POST',
                                  'location': 'LOCALIZAÇAO', 'video_duration': 'VIDEO DURAÇAO',
                                  'shortcode': 'SHORTLINK', 'id': 'ID POST'})

    except:
        d = {'nome': [res], 'status': ['ERRO']}
        dfv = pd.DataFrame(d)

    return dfv




