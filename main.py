import os
from dotenv import load_dotenv
from happylth import Happylth

load_dotenv()

user_id = os.environ['USER_ID']
user_password = os.environ['USER_PASSWORD']
company_path = os.environ['COMPANY_PATH']

hap = Happylth(user=user_id, password=user_password, company_path=company_path)

payload = hap.generate_inputrecord_payload()

# 歩数
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_walkCount'] = '6000'
# 生活習慣チャレンジ /「できた」が1、「できなかった」が0
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio0'] = '1'
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio1'] = '1'
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_radio2'] = '1'
# 体重(kg)
payload['_bohcchallengeinputrecord_WAR_BOHCChallengeportlet_weight'] = '75.1'

hap.post_inputrecord(data=payload)
