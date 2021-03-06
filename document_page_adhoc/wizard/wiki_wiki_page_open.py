# -*- coding: utf-8 -*-


from osv import osv

class wiki_wiki_page_open(osv.osv_memory):
    """ wizard Open Page """

    _name = "wiki.wiki.page.open"
    _description = "wiz open page"

    def open_wiki_page(self, cr, uid, ids, context=None):

        """ Opens Wiki Page of Group
        @param cr: the current row, from the database cursor,
        @param uid: the current user’s ID for security checks,
        @param ids: List of open wiki page’s IDs
        @return: dictionay of open wiki window on give group id
        """
        if context is None:
            context = {}
        group_ids = context.get('active_ids', [])
        for group in self.pool.get('wiki.groups').browse(cr, uid, group_ids, context=context):
            value = {
                'domain': "[('group_id','=',%d)]" % (group.id),
                'name': 'Wiki Page',
                'view_type': 'form',
                'view_mode': 'form,tree',
                'res_model': 'wiki.wiki',
                'view_id': False,
                'type': 'ir.actions.act_window',
            }
        if group.method == 'page':
            value['res_id'] = group.home.id
        elif group.method == 'list':
            value['view_type'] = 'form'
            value['view_mode'] = 'tree,form'
        elif group.method == 'tree':
            view_id = self.pool.get('ir.ui.view').search(cr, uid, [('name', '=', 'wiki.wiki.tree.children')])
            value['view_id'] = view_id
            value['domain'] = [('group_id', '=', group.id), ('parent_id', '=', False)]
            value['view_type'] = 'tree'

        return value

wiki_wiki_page_open()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
