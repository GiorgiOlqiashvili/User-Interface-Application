def sort_entries(entries, sort_by='id'):
    if sort_by == 'id':
        return sorted(entries, key=lambda x: x['id'])
    elif sort_by == 'memo':
        return sorted(entries, key=lambda x: x['memo'])
    else:
        return entries
