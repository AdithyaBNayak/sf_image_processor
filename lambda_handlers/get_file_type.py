

def get_file_type(event,context):
    file_name = event.get('s3',{}).get('object',{}).get('key','')

    if not file_name:
        return
    
    last_index = file_name.rfind('.')
    if last_index in (-1,len(file_name)-1):
        return

    file_type = file_name[last_index+1:]

    return file_type
